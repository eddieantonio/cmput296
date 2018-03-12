% Lab 8: Intermediate JavaScript
% CMPUT 296; written by Eddie Antonio Santos
% March 12, 2018

Overview
========

 - Become familiar with JavaScript objects
 - Become familiar with JavaScript's


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


wat.js
------

<blockquote cite="http://www.stroustrup.com/blast.html">
<p>There are only two kinds of programming languages: those people always
[complain] about and those nobody uses.</p>
<cite>[Bjarne Stroustrup](http://www.stroustrup.com/blast.html), Creator of C++</cite>
</blockquote>

As a warm-up exercise, we'll explore the more infamous aspects of
JavaScript, such as its **weak typing**, **type coercion**, and using
IEEE 754 **double-precision floating point** numbers as its built-in
numeric type.


### wat: Type coercion and weak typing

<aside>
Note that "weakly-typed" and "strongly-typed" is more of a continuum
than a dichotomy; a programming language can be sometimes weakly-typed
and sometimes strongly-typed. For example, Python 3 will convert between
`int` and `float` automatically, and has "truthy" and "falsey" values,
but is strongly-typed in that it does not allow automatic conversion
between strings and numbers, and it does not like to mix byte and
Unicode strings.
</aside>

**Type coercion** is the automatic conversion from one data type to
another in programming languages without necessarily requesting it.
Languages that perform implicit type conversions like this are often
called **weakly-typed**, because they translate between data types
without the programmer explicitly requesting any type conversions.
Conversely, a programming language that _requires_ the programmer
specify when to convert between data types---say when converting between
a string and a number---is called a **strongly-typed** programming
language.

<!-- try prompt: prompt for a number -->

Let's determine whether JavaScript is a **weakly-typed** or
**strongly-typed** language.

In Google Chrome, on any webpage, open up the [DevTools JavaScript
Console][console] (Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd>
+ <kbd>J</kbd>; macOS: <kbd>Cmd</kbd> + <kbd>Alt</kbd> + <kbd>J</kbd>).

[console]: https://developers.google.com/web/tools/chrome-devtools/console/?hl=en


We're going to write a very small program that determines how old you
are. Type the following into the Console:

```javascript
var birthYear = prompt("What year were you born?");
```

Answer the prompt by typing an appropriate **positive integer** (e.g.,
I would have written `1992` in the prompt).

> **Question 1**: What is the type of the variable `birthYear`?

Now type the following:

```javascript
var yourAge = (new Date()).getFullYear() - birthYear;
```

> **Question 2**: What is the type of the variable `yourAge`?

Now finish it by writing a line of code that will print how old you are:

```javascript
var output = "You are " + yourAge + " years old";
console.log(output);
```

> **Question 3**: Did JavaScript perform any implicit type conversions?
> How many type conversions and where?

> **Question 4**: Write the same small program in Python (asks for your
> birth year, calculates your age, prints it in a sentence). Use
> `input()` and `print()` instead of `prompt()` and `console.log()` (you
> may hard code the current year instead of using the `datetime`
> module). Make sure your program works, and copy-paste it as the answer
> to this question.

> **Question 5**: Is JavaScript more of a **weakly-typed** language or
> a **strongly-typed** language? Provide code to justify your answer.

> **Question 6**: State one **advantage** of weak typing.

> **Question 7**: State one **disadvantage** of weak typing.


### How to avoid it use: `===` and `!==`


### wat: IEEE 754 floating point

JavaScript's default numeric type is [IEEE
754](https://en.wikipedia.org/wiki/IEEE_754) Binary64 "double precision"
floating point format. This number representation is available as the
`float` type in Python and is (usually) the `double` type in C/C++.

Quick facts about floating points:

 - numbers are _approximations_ of (real numbers)
 - includes many finite values, two infinities, and lots of NaN.


<!--
Forgetting var; creating a global

NaN

nan in Python. nan in C.
-->


<!-- at what power of can you no longer -->

<!--
triple equal
-->

<!--
make them define a Python class, method, and then do the

>>> whoami(object.method())

print(type(self))


Do the same thing in JavaScript

class Herp {
   derp() {
      console.log(this);
   }
}

>>> whoami((new Herp).derp)

Use Function.bind(obj)

-->

<!--

 Automatic semicolon insertion

function hello() {
  return
  {
    foo: "bar"
  }
}

-->

Along the way, we'll be learning how to use Chrome's
JavaScript debugger.
We'll explore **first-class functions** (a.k.a., "**closures**", or "**lambdas**"),

```js
function cons(a, b) {
  return function (m) {
    return m(a, b);
  };
}

function car(cell) {
  return cell(function(a, b) {
    return a;
  });
};

function cdr(cell) {
  return cell(function(a, b) {
    return b;
  });
};
```

<!-- how to debug: debugger; -->
