Title: Javascript modules
Summary: Using javascript modules in browser and its implications
Category: Coding
Date: 2020-01-29
Updated: 2020-07-07
Status: published
Author: Tomas Peterka

Javascript modules do not write into global namespace. That is the main difference and it requires you to change your mindset about
running javascript on your site. Usually, the javascript that you have included in your site created some globally available objects. 
A great example is `$` of `jQuery` that is placed directly to global `window` object. This still works with modules - only `var`s
defined in modules will not spoil the global namespace.

You have to specify your dependencies. If the dependencies write to the global namespace then, for sake of clarity, you should call your module inline from HTML 
because only there you are sure the global object exists. The usage of global object should be close to the "include" is done using another `<script>` tag.

If you decide to use modules, then your HTML code will look as follows 

```javascript
// file s1.js
const output = console.log;

export default output;
```

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Test</title>
</head>
<body>
	<script type="module">
		import output from "./s1.js"; // no prior <script src="s1.js"> necessary
		output("hello");
	</script>
</body>
</html>
```

notice `type="module"` in both `<script>` declaration. That allows some magic to be performed

 * automatic `fetch` of relative imported (java)scripts
 * support for import/export statements

Javascript is transiting from something that was inlined inside HTML into an application programming language.
So where is the border between inlining and a single-page web application? My decisioning rule is actually simple. 

> If you have two entities on the page that need to be notified about each other events then you need a web app.  

Every framework has their own way of solving horizontal communication. I am no framework guru so I cannot elaborate. I have my preferred way
though is using native web components and communicate via CustomEvents dispatched on document root. The advantage of that is that you don't
need any framework (even though I use lit-element to ease the development a bit). An example might be my first and definitely not last [project](projects/webdave.html)
that uses this CustomEvents technique. I am so content with this way of building framework independent web apps that I call this technique modestly "the Web API".

