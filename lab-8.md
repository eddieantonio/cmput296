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

 - Google Chrome's [DevTools]
 - An internet connection
 - A text editor
 - A Python 3.5+ interpreter that can be run from the command line.
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

<!-- talk about DOM manipulation first? -->

Asynchronous programming
------------------------

In this lab, the goal is to make a request to an external server
**without** navigating away from the current webpage.

In order to do this, it is vital to understand **asynchronous
programming**.


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

The program will call the `add()` function _immediately_.

However, you, as a programmer, have no control over user interaction, or
at what moment, exactly, an external server replies to you (if at all).
For example, the developers of Facebook Messenger have no control if
or when a user will write a message to someone and send. Yet, the
developers of Facebook want you to be able to send a message at _any
moment_ without navigating away from the page. This is an example of an
_asynchronous event_. "Asynchronous" means that the event may not be
initiated by your action, as a programmer. Rather, an external event
may initiate an action at any moment, and you, as a programmer, must
declare a way to **react** to that event.


### Asynchronous programming in JavaScript

<aside>
Just as in [Lab 6](./lab-6.html),
if you are security conscience, you should verify that the SHA-256
checksum of `server.py` that you downloaded matches the checksum that
I computed:

```
334e487a26471a1724d22da4b5418efba63ad2a0b1eb269cf5e989bf3be08058
```

Use [`sha256sum`](https://help.ubuntu.com/community/HowToSHA256SUM) to verify that the file you downloaded has the same
SHA-256 checksum. Please peruse the source code to ensure it is not malicious in nature.
</aside>

Before please, download
<a href="lab-8/server.py" download><code>server.py</code></a> and
<a href="lab-8/index.html" download><code>index.html</code></a>.
Place these files in the same directory.

Now, open up a terminal and navigate to the directory in which you
downloaded the files. Start the server by typing:

```sh
python3 server.py
```

Enter in values for `a`, `b,` and use the drop-down to select an
arithmetic operation.

> **Question X**: What happens when you press the "Calculate" button?



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

