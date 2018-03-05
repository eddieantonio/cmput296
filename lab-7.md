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

> **Question X**: Questions look like this.

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
console. On _any_ webpage, open up the [DevTools JavaScript
Console][console] (Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd>
+ <kbd>J</kbd>; macOS: <kbd>Cmd</kbd> + <kbd>Alt</kbd> + <kbd>J</kbd>).

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

<!-- Don't just tell people about mistakes; make them do it. -->

Basic JavaScript
----------------

As in the Python console, you can use the JavaScript console to run
code. Try the following in the JavaScript console:

```javascript
7 / 2;
```

> **Question 2**: What value did `7 / 2;` return? Is this an integer
> or a floating-point value?

Define a variable in the JavaScript. Write the following in the
JavaScript console:

```javascript
var hello;
```

This defined a variable called `hello`. Notice how we have not
_assigned_ anything to the variable yet.

Now, simply type the name of the variable to get back its value in the
JavaScript console.

```javascript
hello;
```

> **Question 3**: What value did `hello;` return?

Try the following in the JavaScript console.

```javascript
hello = "world";
hello.toUpperCase();
hello;
```

> **Question 4**: Using your knowledge of Python and other programming
> languages, explain what you assume the last three lines of JavaScript
> may have done, in as much detail as possible.

Embedding JavaScript in a webpage
---------------------------------

We'll learn how to include JavaScript in a web page. Copy the following
minimal HTML and call it `js-example.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title> JavaScript example </title>
</head>
<body>

</body>
</html>
```

Open `js-example.html` in Google Chrome/Chromium. In the same directory
as `js-example.html`, create a new, empty file called `food.js`.

We will write a small JavaScript program that takes input, and prints it
back out, in a message. This `food.js` will ask you what your favourite
food is, and then `alert()` it back out at you. Start with the following
code:

```javascript
var faveFood = prompt("What is your favourite food?");

// TODO: use alert() to print "Your favourite food is <FOOD>!".
```

Write JavaScript code that uses `alert()` to print a string that says
"your favourite food is `<FOOD>`!" where `<FOOD>` is the whatever the user
input into the `prompt()`.

Now we must include this JavaScript file in the page.

To include an **external JavaScript file** in an HTML document, you must
add `<script>` element, like the following:

```html
<script src="path/to/your/file.js"></script>
```

Note that this line contains both a start `<script>` tag and a closing
`</script>` tag. You may know refresh `js-example.html` to see if your
code worked.

> **Question 5**: What is the appropriate `<script>` tags that you
> should use to include `food.js` into `js-example.html`?

> **Question 6**: Where in your HTML page should you put the
> `<script></script>` tags? (Within what element?) Why is this the most
> appropriate place to put include the JavaScript?

> **Question 7**: The `<script>` tags looks like it should be a void
> element (like `<link>` or `<img>`), but is it? Try using
> a self-closing tag like `<script src="..." />`. Does the code still
> work when using a self-closing tag?

With `food.js` referenced within `js-example.html`, test that `food.js`
works before continuing. As a reminder, each time you load
`js-example.html`, it should ask you what your favourite food is, and
then it print it back out in a formatted message using `alert()`.

> **Question 8**: Copy-paste your finished version of `food.js` as the
> answer to this question.

Let's extend the program we wrote for **Question 8**. Now, it will check
if the user's favorite food is `"pupusas"`. If so, it will say:
"Yay! Pupusas are my favourite too!".


Extend `food.js` with an `if` statement. `if` statements look like this
in `JavaScript`:

```javascript
if (/* condition */) {
   /* consequent */;
}  else {
   /* alternative */;
}
```

In this case, the alternative will be the same as what we printed in
**Question 8**. The consequent should `alert()`, "Yay! Pupusas are my
favourite too!".

As with Python, you can compare strings simply using the `==` ("double
equals") operator; unlike Python, you may compare strings using the
`===` ("triple equals") operator.

In `food.js`, write the code to `alert()`, "Yay, Pupusas are my
favourite too!" if what the user typed into the `prompt()` was
"pupusas" (all lowercase, with no extraneous whitespace). Save the file
and reload `js-example.html`. Try the prompt once with "pupusas" and
reload the page with and input a different food this time. Make sure the
code works as intended.

> **Question 9**: Copy-paste your working `if`/`else` statement from
> `food.js` as the answer to this question.


> **Question 10**: Rewrite the `if` condition such that it disregards
> differences in capitalization (such as `"Pupupas"`) and extraneous
> whitespace (such as `"   PUPUSAS  "`) when deciding whether the user
> input `pupusas`. Suggestion: Look through MDN's list of
> [`String` methods][string methods] to find methods that will help
> normalize letter case and remove extraneous whitespace. Copy-paste
> your new `if`/`else` as the answer to this question.


[string methods]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#String_instances

Functions
---------

Let's _refactor_ our code so that it is contained completely inside
a function.

```javascript
document.onload = function () {
};
```


`for`-loops
-----------


<!-- for loop -->

<!-- how to include inline JavaScript -->

```html
<script>
</script>
```

> **Question X**: Use your experience writing JavaScript to answer the
> following question. In terms of _syntax_ (the structure of the code:
> the use of punctuation, semicolons, whitespace, etc.), is JavaScript
> more like **Python** or **C/C++**? In terms of _semantics_ (the
> meaning of code: how variables are interpreted, when types are
> considered, memory management, etc.) is JavaScript more like
> **Python** or **C/C++**?
