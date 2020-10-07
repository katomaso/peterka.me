Title: WebDAV editor
Category: Projects
Summary: Web-Component editor using webDAV as its backend
Slug: webdave
Status: draft
Date: 2019-12-25

I started this project so I can write my personal pages vie web. Nothing special you say?
My sites are generated using static site generator (getpelican.com). It is annoying to SSH
and edit content using Vim. Especially when you allowed only key sign in on the server.

This project has a few interesting apects
- it is implemented using web components (using lit-element as the most low-level library that ease day-to-day tasks with web components)
- no specific backend is required (nginx/caddy is enough)
- can be reused by anyone - correct web server configuration is enough
- can be extended by anyone - the API are `CustomEvent` instances dispatched on `document`

Sounds simple in theory, right? Let's get into details. The main adversary here will be CORS.

## Configuring WebDAV for CORS

If you want to use webdav editor for yourself then you need to configure your webdav server
so it points to the source of your posts. Main touble here is CORS. Firstly, I used lighttpd
that could force HTTP Reponse 2xx on preflight OPTION request. That was not the case for
nginx's third-party module `webdavExt`. But then a new issue arrised with lighttpd - it
always return 4xx response on OPTION request on non-existing files.Browsers always do this
request before any other - even POST request that is to create a new file. Browser of course
disallow my beautiful POST request when OPTION did not return 2xx. I filled an issue (request)
on lighttpd's issue tracking and after a few arguments https://redmine.lighttpd.net/issues/2939
the issue got resolved! Yay! Unfortunately lighttps does not set `Cache` headers for "binary"
files. Sounds ok right? But Lighttpd considers Markdown files as binaries. Therefor I turned
away from lighttpd and chose a new version of Nginx that fixes webdav's problem with PROPFIND
request that was not considering CORS headers set in configuration. https://stackoverflow.com/questions/54523895/nginx-webdav-module-ignoring-cors-headers

Luckily, nginx (1.14.0 an on) can handle CORS responses and headers correctly
for WebDAV module if you use `always` keyword in add_header. Please take a look on the final
nginx configuration. This configuration has two cool features. First is that it allows CORS
for any of my subdomains and localhost. Second is that it sends allowed headers header only
for preflight OPTION requests. Others require only allow origin header.


```
server {
    listen               <ip>:443 ssl;
    server_name          webdav.peterka.me;
    ssl_certificate      <certificate-path>;
    ssl_certificate_key  <key-path>;

    access_log  /var/log/nginx/webdav.peterka.me.access.log;

    dav_methods       PUT DELETE MKCOL COPY MOVE;
    dav_ext_methods   PROPFIND OPTIONS;

    autoindex             on;
    create_full_put_path  on;
    dav_access            user:rw group:rw all:rw;
    auth_basic            "restricted";
    auth_basic_user_file  <passwd-path>;

    set $cors_methods "GET, HEAD, POST, PUT, OPTIONS, MOVE, DELETE, COPY, LOCK, UNLOCK, PROPFIND";
    set $cors_headers "Authorization, Origin, Content-Type, Accept, Keep-Alive, User-Agent, If-Modified-Since, Cache-Control, Content-Range, Range, Depth, Content-Length";

    location / {
        root /srv/http/content/;

        if ($http_origin ~* '^http://localhost(:[0-9]+)?$') { # localhost from any port (is part of the http_origin)
            set $cors "matched";
        }
        if ($http_origin ~* '^https://([a-z]+\.)?github\.io$') {  # any github page (such as katomaso.github.io) 
            set $cors "matched";
        }
	    if ($request_method = OPTIONS) {
            set $cors "${cors} & preflight";
        }

        if ($cors = "matched") {
            add_header Access-Control-Allow-Origin "$http_origin" always;
        }
        if ($cors = "matched & preflight") {
          add_header Access-Control-Allow-Origin "$http_origin" always;
          add_header "Access-Control-Allow-Methods" $cors_methods;
          add_header "Access-Control-Allow-Headers" $cors_headers;
          add_header Content-Type text/plain;
          add_header Content-Length 0;
	      return 204;
	    }
    }
}
```