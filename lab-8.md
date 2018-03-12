% Lab 8: JavaScript: type coersion, arrays, and objects
% CMPUT 296; written by Eddie Antonio Santos
% March 12, 2018

Overview
========

 - Become familiar with JavaScript's type coercion
 - Learn how to use JavaScript's arrays
 - Define "classes" in three different ways in JavaScript


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

In this lab, we'll explore intermediate features of the JavaScript
programming language.

### Type coercion and weak typing

<blockquote cite="http://www.stroustrup.com/blast.html">
<p>There are only two kinds of programming languages: those people always
[complain] about and those nobody uses.</p>
<cite>[Bjarne Stroustrup](http://www.stroustrup.com/blast.html), Creator of C++</cite>
</blockquote>

As a warm-up exercise, we'll explore **type coercion** in
JavaScript.

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


### Arrays

An empty array in JavaScript is written like this:

```javascript
var arr = [];
```

An array with four elements is written like this:

```javascript
var arr = ["one", "two", "three", "four"];
```

Like Python, array elements can be accessed using index notation.

```javascript
> arr[0];
"one"
```

To get the length of an array, use its `.length` property:

```javascript
arr.length
> 4
```

Try the following lines in the JavaScript console and observe the
results:


```javascript
var arr = ["one", "two", "three", "four"];
arr.push("five");
arr;
arr.pop();
arr;
arr.unshift("zero");
arr;
arr.shift();
arr;
```

> **Question 14**: For each of the following methods: `.push()`, `.pop()`,
> `.unshift()` and `.shift()` explain what they do, and what they
> return.

> **Question 15**: Are arrays mutable or immutable? Explain your
> answer.

To iterate over arrays in JavaScript, it may be tempting to do this:

```
var arr = ["one", "two", "three", "four"];
for (var thing in arr) {
  console.log(thing)
}
```

> **Question 16**: Is `thing` bound to each object in the array, or each
> index of the array?

Try the following lines in the JavaScript console and use the
results to answer questions **17** and **18**.

```javascript
var arr = ["one", "two", "three", "four"];
arr.five = 5;
```

> **Question 17**: What are the contents of `arr` now? Is this what you
> expect? What does this imply about JavaScript arrays?

> **Question 18**: What happens when you use a `for (... in ...)` loop
> on `arr`? That is, if you ran the following loop:
>
>     var arr = ["one", "two", "three", "four"];
>     for (var thing in arr) {
>       console.log(thing)
>     }
>
> What does it print and why?


<!--

```javascript
class Complex {
  constructor(real, imag) {
    this.real = real;
    this.imag = imag;
  }

  toString() {
    return this.real.toString() + '+' + this.imag.toString() +'i';
  }
}
```
-->



[parseInt]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt#Syntax
[parseFloat]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#Syntax
