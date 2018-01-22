% Lab 1: URLs
% CMPUT 296; written by Eddie Antonio Santos
% January 22, 2018

Overview
========

 - Use your browser's developer tools to investigate HTTP
 - Learn about HTTP requests and responses
 - Learn about HTTP status codes
 - Learn about HTTP headers


Materials
=========

 - Google Chrome/Chromium (the instructional staff does not officially
   provide support for other browsers, although all major modern
   browsers have comparable functionality)
 - An internet connection


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**. Questions look like this.

**Remember to cite your sources**.


Introduction
------------

A common job interview question is,

> In as much detail as possible, describe what happens after I type
> "example.com" in my browser and press <kbd>Enter</kbd>.

In this lab, we will investigate one crucial component of this process:
the Hypertext Transfer Protocol (HTTP). To do this, we will open up
[Google Chrome's DevTools][devtools].

To access these Chrome's DevTools from any open tab, do one of the
following following:

 * (Linux/Windows) Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>
 * (macOS): Press <kbd>Cmd</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>
 * (Any platform) Click the main drop-down menu > "More Tools" > "Developer Tools"

[devtools]: https://developers.google.com/web/tools/chrome-devtools/

The DevTools may appear "docked" to the bottom of your browser window,
docked to the right side of the window or as a new window entirely. Use
whichever configuration you find most convenient.

The rest of the lab will assume the following:

DevTools are open on the **Network** tab:

![Clicking on DevTools Network tab](./lab-2-open-network-tab.png)

In the **Network** tab, **Disable Cache** is clicked.

![Clicking on "Disable cache"](./lab-2-disable-cache.png)

Investigating an HTTP request
-----------------------------

With the DevTools open, in the same browser tab navigate to
`http://example.com`.
