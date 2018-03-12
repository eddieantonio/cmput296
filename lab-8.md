% Lab 8: JavaScript: type coersion, and objects
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


Intermediate JavaScript
-----------------------

In this lab, we'll explore some of the more esoteric features of the
JavaScript programming language. Along the way, we'll be learning how to
use Chrome's JavaScript debugger.


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

Now finish it by writing a two lines of code that will print how old you
are:

```javascript
var message = "You are " + yourAge + " years old";
console.log(message);
```

> **Question 3**: Write the same small program in Python (asks for your
> birth year, calculates your age, prints it in a sentence). Use
> `input()` and `print()` instead of `prompt()` and `console.log()` (you
> may hard code the current year instead of using the `datetime`
> module). Make sure your Python program works, and copy-paste it as the
> answer to this question.

> **Question 4**: Did JavaScript perform any implicit type conversions?
> How many type conversions and where?

> **Question 5**: Try the JavaScript version again, but this time,
> instead of entering your birth year as a positive integer in the
> `prompt()`, write it out in English (e.g., `nineteen-ninety-two`).
> What is the output of the `console.log()`? Is this different than
> what you expected? Explain.

Try the following lines in the JavaScript console and observe the
results:

```javascript
1 == '1';
0 == '';
1 == true;
70 == '0x070';
+'42';
+'0xbadbeef';
+'0xgoodbeef';
```

> **Question 6**: What is the result of each line of code? Did any of
> the results surprise you?

> **Question 7**: What is the type of this expression?
>
>     "42"
>
> What is the type of this expression?
>
>     +"42"
>
> What is the type of this expression?
>
>
>     +"forty-two"

> **Question 8**: Explain the behaviour of the following JavaScript
> expression:
>
>     70 == '0x070';
>
> Why does it return what it returns?

Use your experimentations in the previous section to justify the
following questions.

> **Question 9**: Is JavaScript more of a **weakly-typed** language or
> a **strongly-typed** language? Provide code to justify your answer.

> **Question 10**: State one **advantage** of weak typing.

> **Question 11**: State one **disadvantage** of weak typing.


### How to avoid confusion: `parseInt()`, `parseFloat`, `===` and `!==`

Whenever you are converting from a string to a number, use the
[`parseInt()`][parseInt]
and
[`parseFloat()`][parseFloat]
functions as appropriate.


> **Question 12**: Rewrite the first line of the JavaScript program
> (i.e., `var birthYear = prompt("What year were you born?");`)
> using either `parseInt()` or `parseFloat()` (which ever you think is
> most appropriate. Paste this revised line of code as the answer to
> this question. What will happen if I enter in my birth year as
> `0x1992` into the prompt?

When comparing items of different types, use the
**strict equality operators**: `===` and `!==`.

> **Question 13**: In JavaScript, what is the difference between
> the output and meaning of the following two statements?
>
>    1 == true;
>
>    1 === true;

### wat: IEEE 754 floating point

JavaScript's default numeric type is [IEEE 754][] Binary64 "double precision"
floating point format. This number representation is available as the
`float` type in Python and is (usually) the `double` type in C/C++.

Quick facts about floating points:

 - numbers are _approximations_ of (real numbers)
 - includes many finite values, two infinities, and lots of **NaN**.

[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754

Since there are a limited number of whole numbers that can be precisely
represented using IEEE 754 floats, arithmetic becomes counter-intuitive
as the numbers become more and more extreme.

For example, in double-precision floating points, numbers, adding 1 to
a number no longer works as you would expect when the one of the numbers
is sufficiently large. For example, try this in your favourite language
with floating point numbers (I'm using Python:

```python
>>> 1000000000000000000.0 + 1
1e+18
>>> 1000000000000000000.0 + 1 == 1000000000000000000.0
True
```

However, for small whole numbers, this arithmetic works as you would
expect:

```python
>>> 100.0 + 1
101.0
>>> 100.0 + 1 == 100.0
False
```

Let's find the point at which arithmetic stops making sense.
Write a JavaScript program that outputs the **minimum
power of 2** at which adding 1 to a number no longer works as expected.
That is, at what value of *n* is this expression true?

    (2 ** n + 1) === (2 ** n)

> **Question 14**: Copy-paste your program as the answer to this
> question.

> **Question 15**: At what power of 2 does adding one to a number no
> longer work as expected?


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

[parseInt]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt#Syntax
[parseFloat]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#Syntax
