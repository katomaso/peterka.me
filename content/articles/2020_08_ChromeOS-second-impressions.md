Title: ChromeOS second impressions
Summary: After a few months of usage of ChromeOS, I am still really impressed.
Category: Articles
Date: 2020-09-09
Updated: 2020-09-29
Author: Tomas Peterka

## Web applications

ChromeOS let's you run primarily only [web apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps). Such applications 
are written in javascript, run in your web browser and seldom send anything over the internet. Those applications tend to be offline 
first - meaning that they use browser's storage options. You can say a page is serving you a web app when you can find reference to an app manifest
```html
<link rel="manifest" href="/manifest.webmanifest">
```
First and most important web app offline technology is [Service Worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API).
It is a piece of javascript code that gets installed into your browser. This is very similar to installation of regular old-time application.
Service Worker would install all necessary assets along with it such as images, html and other code.  
Second important storage is browser's Local Storage for files and IndexedDB for structured data. Browser gives an app (by default) 4GB of storage.
This is enough storage to accomodate a complex aplication! Meaning that even large applications can be written as web apps. Of course, performance
of javascript in a web browser must be taken into account so not-so-complex applications. In order to increase performace, you would use WebAssembly
that I do not want to cover in this post. But I do think it will be important for certain class of applications.

## Graphics editing

I faced the issue that I needed to apply "Color to Alpha" filter in one image. I think it is called "keying" in video processing. A few weeks later
I needed to compose three pictures together. I was tempted to install [GIMP](https://gimp.org/) in linux container and get the work off the table.
But then I remebered why I bought a ChromeBook in the first place and looked around the internet. Guess what I have found! A complete copy of GIMP
written as a web app - an amazing piece of software called [Photopea](https://photopea.com/) that let you edit graphics on a decent level inside your
browser. It replaces GIMP fully and even partially Photoshop!

## Hardware programming

One day I realized I might need to program Arduino and I have only a ChromeBook at hand! Arduino, for the ones who don't know, is a simple piece of
electronics that you connect via USB to your computer and you can upload a very simple program (written in C) that controlls inputs/outputs of the
chip so you can create simple controllers for LED strips or even connect light/proximity/temperature sensors to light or computer output. Seems like
out of league for ChromeBooks. They support only web apps. But given that education is the greatest market for chromebooks and Arduinos are the must-have
electronics for every class-room that is not in middle ages, supporting Arduino was a logical step from ChromeOS. And well - the support is really there!
Seems so that you can program your Arduino directly from your browser using [Arduino's Chrome extension](https://chrome.google.com/webstore/detail/arduino-create/dcgicpihgkmccjigalccipmjlnjopdfe)
An extension is necessary for direct communication with USB ports, no web-app could access hardware on such low-level. If you do not want to pay the dollar
a month for the extension and related cloud storage for programming your Arduinos, I suppose you cann still get by with traditional Arduino's IDE running 
in a linux container. Direct USB connectivity from the container is "the next thing" in ChromeOS development, currently hidden under an experimental switch.

## Video

I came across a restriction about video formats playable directly from the disk. For example MKV container that features audio in some non-web-standard
format will not get played. I think that DVD-quality AAC could not be played. This is a constraint that you need to be aware of - only web-standardized
audio/video can be played off the disk because ChromeOS uses the same player that is available in the browser.