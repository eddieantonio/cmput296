% Lab 7: Introduction to JavaScript
% CMPUT 296; written by Eddie Antonio Santos
% March 5, 2018

Overview
========

 - Learn how to embed JavaScript in the browser
 - Learn basic JavaScript syntax
 - Learn how to debug JavaScript


Materials
=========

 - Google Chrome's [DevTools]
 - A text editor

[DevTools]: https://developer.chrome.com/devtools


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**. Questions look like this.

**Remember to cite your sources**.


Introduction to JavaScript
--------------------------

JavaScript (also known by its standard name, [ECMAScript]) is the
programming language embedded in most modern web browsers. In this lab,
we'll explore how to write and run JavaScript in our own web pages.

[ECMAScript]: https://www.ecma-international.org/publications/standards/Ecma-262.htm


Using the JavaScript console
----------------------------

A helpful way to practice JavaScript is to experiment in the interactive
console. Open up the [DevTools JavaScript Console][console]
(Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>;
macOS: <kbd>Cmd</kbd> + <kbd>Alt</kbd> + <kbd>J</kbd>).

![Opening the JavaScript console](./lab-7/console-open.png)

[console]: https://developers.google.com/web/tools/chrome-devtools/console/?hl=en

In the console, type the following:

```javascript
alert("Hello, World!");
```

Now, type the following:

```javascript
console.log("Hello, World!");
```

> **Question 1**: What did each line do? If you were casually browsing
> a webpage, which one of `alert()` or `console.log()` would be less
> intrusive?



<!-- Try to keep this one to the console? -->
<!-- Don't just tell people about mistakes; make them do it. -->

<!-- how to alert() -->

<!-- how to debug: console.log() -->
<!-- how to debug: debugger; -->

<!--

(syntax, if statement, for loop, lambos)

syntax, curly bracket, for loop, semicolons, ===

declare a variable

-->


<!-- Lambos -->

```javascript
document.onload = function () {
};
```

<!-- how to include JavaScript -->
```html
<script src=""></script>
```

<!-- how to include inline JavaScript -->

```html
<script>
</script>
```
