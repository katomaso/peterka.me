Title: API on the Web
Date: 2018-04-10
Modified: 2018-10-01
Category: Articles
Author: Tomas Peterka
Status: draft
Summary: API itself on connected applications is not enough. API need to have a machine-readable description to be auto-discoverable.

# What is an API
API (Application Programming Interface) shows capabilities of your aplication to the outside world.  

-  **libraries** define their API in header files and/or in the .dll/.so files themselves;  
-  **applications** define their API by set of binaries and their command line arguments;
-  **web application** ?

API of web applications is a tricky topic because those applications are crafted for human interaction.
In fact, there is only one specificity to every web application - their URL set. For example application
runnig on `a.example.com` will have valid URLs `/foos`, and `foos/1` but application running on `b.example.com`
will have valid URLs `bars`, and `bars/1`. Therefor we can conclude that Web Application Interface is specified
by discoverable internal links. Those links can be found either in `a` elements or in `form.target` attribute.


## Web 1.0 
In the past and surviving present, the API was described by URL, Query and HTML. 
You told the server which view you require by typing an `URL`.  
Server told you what the current view is intended for by textual information in paragraphs `<p>`.  
Server told you what `<input>` inputs the view needs in order to serve you well.  
Server told you where to go `<a>` in order to do different actions with current resource.  

## Web 2.0
In the present, API is still described by URL but Query was swapped for Fragment (the part of URL after #)
and POST form data for JSON as a payload. Or by Proto buffers and (g)RPC. Or as SOA by 

## Web 3.0
Nowadays, every developer know what a reverse proxy is. In short, it is one server dispatching requests to many services.
Recently, NGINX [introduced Unit](https://www.nginx.com/blog/nginx-unit-1-0-released/), a programming bus with
one - HTTP/2.0 interface. [New databases](http://couchdb.apache.org/) are being built with simple HTTP/JSON interface.
More distributed services like microblogging/distributed social networks like Mastodon, GNU-Social using standardized social API.
Distributed communication tools (Matrix) are being created. Not mentioning the whole Blockchain hype. Architecture is obviously
moving towards distributed, serverless computation. Why? Because now we can. Hardware is getting smaller and more
affordable. Why again? Because it is easier to change and test separate small parts.

My guess about the future.

I suppose that one server will export 

Browser already supports rendering of multiple gadgets. Imagine 
There are few ways of describing the API of your application.