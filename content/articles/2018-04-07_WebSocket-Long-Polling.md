Title: WebSockets versus Long Polling versus EventSource
Summary: Article mainly for myself to make sense in those technologies
Category: Articles
Date: 2018-04-20
Author: Tomas Peterka

## WebSocket

WebSocket is initiated by the browser. It sends HTTP**/1.1** request to the server with special header

```
  Upgrade: websocket
  Connection: Upgrade
  ...web-socket specific headers...
```

and the server responds with `HTTP101: Protocol Upgrade` and switches to the WebSocket
protocol which is different from HTTP! They have only one thing in in common - both work over TCP.
Obviously you need a special server to handle the WebSocket (ws:// or wss://) protocol because standard
HTTP frameworks cannot.

Use WebSocket for high-frequency communication between browser and server.


## EventSource (a.k.a. HTML5 Server Sent Events)

EventSource is standard HTML5 uni-directional implementation of server push method. The browser opens one **persistent**
HTTP connection to the server via javascript's `var stream = EventSource.open(....)`. This connection is open
until explicitly `stream.close()`d. EventSource allows only to receive data in `Content-Type: text/event-stream` (simple text).

On server side we simply write&flush into the one opened connection. Of course header `Cache-Control: no-cache` is advisible
on the server side.

Use EventSource for high-frequency push notification.


## Long Polling

Long Polling is a poor's man feature (or a hack if you please). It is simply a request with a long timeout for the response.
Client issues such request and waits until server sends some data when they become available. Righ after receiving
the data client issues a new long request.

It differs from Event Source in two things. First, it does not keep one connection open but makes a sequence of connections.
Second, since it is (limited) bi-directional connection then you can send data to the server after every response.
 
Long Polling is obviously meant for work-everywhere but high latency communication. Each message is a complete HTTP 
request/response round. It is "bidirectional" in the way that it is the client who always issues a request and receives
exactly one response. This repeats indefinitely.

Many of you have heard about [HTTP/2.0 Push](https://en.wikipedia.org/wiki/HTTP/2_Server_Push) but that is something 
completely different. The name is unfortunate IMHO.
HTTP/2.0 Push only sends more files than requested because the server knows that the client would ask for them in
following request. This feature is used to send static files together with HTML file.

Use Long Polling for bi-directional communication when WebSocket is not available. 

## Links

[Comparison by implementation](http://www.dsheiko.com/weblog/websockets-vs-sse-vs-long-polling)