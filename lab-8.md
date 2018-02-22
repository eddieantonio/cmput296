% Lab 8: Asynchronous JavaScript and XMLHttpRequest (AJAX)
% CMPUT 296; written by Eddie Antonio Santos
% March 18, 2018

Overview
========

 - Learn about asynchronous programming in JavaScript
 - Learn the API for `XMLHttpRequest`
 - Perform some asynchronous DOM manipulation

Materials
=========

 - An internet connection
 - Google Chrome's [DevTools]
 - Included files:
   <a href="lab-8/server.py" download><code>server.py</code></a>,
   <a href="lab-8/index.html" download><code>index.html</code></a>

[DevTools]: https://developer.chrome.com/devtools


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**. Questions look like this.

**Remember to cite your sources**.

<!-- goal: make a valid XHR. Put it in a <div> -->

Asynchronous programming
------------------------

In this lab, the goal is to make a request to an external server
**without** navigating away from the current webpage.

In order to understand to perform this, it is vital to understand
**asynchronous programming**.

### What is "asynchronous programming"?

In typical procedural programming, the programmer is often in control of
the exact flow of instructions. That is, you, as the programmer say:

```js
if (x < 0) {
  return 0;
}
```

And the program will _immediately_ test if `x` is indeed less than 0,
and then it will execute the consequent as soon as it determines this.

Similarly, if you write JavaScript code that says:

```js
add(2, 2)
```

The program will call `add()` function _immediately_.

However, you, as a programmer, have no control over user interaction, or
at what moment, exactly, an external server replies to you (if at all).
For example, the developers of Facebook Messenger have no control _if_
or _when_ a user will write a message to someone and send. Yet, the
developers of Facebook want you to be able to send a message at _any
moment_ without navigating away from the page. This is an example of an
_asynchronous event_. "Asynchronous" means that the event may not be
initiated by _your_ action, as a programmer. Rather, an external event
may initiate an action _at any moment_, and you, as a programmer, must
declare a way to _react_ to that event.


### Asynchronous programming in JavaScript


<!-- Asynchronous programming -->

<!-- Sending the right headers -->

<!-- Handling the response -->

<!-- Why asynchronous programming? How long does it take to send the
     HTTP request/response? The page pauses while the entire request
     downloads. What would be the consequence on the user experience if
     the page paused? -->

<!--

     http://wiki.c2.com/?HollywoodPrinciple

-->

### DOM manipulation

### `XMLHttpRequest`

