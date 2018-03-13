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
are. Type the following into the JavaScript console:

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

Now finish it by writing two lines of code that will print how old you
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
70 == '70';
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

[parseInt]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt#Syntax
[parseFloat]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#Syntax


> **Question 12**: Rewrite the first line of the JavaScript program
> (i.e., `var birthYear = prompt("What year were you born?");`)
> using either `parseInt()` or `parseFloat()` (which ever you think is
> most appropriate. Paste this revised line of code as the answer to
> this question. What will happen if I enter in my birth year as
> `0x1992` into the prompt?

When comparing items of different types, use the
**strict comparison operators**: `===` and `!==`.

> **Question 13**: In JavaScript, what is the difference between
> the output and meaning of the following two statements?
>
>    1 == true;
>
>    1 === true;


Arrays
------

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
arr.length = 16;
arr;
arr[15] = 'sixteen';
arr;
```

> **Question 14**: For each of the following methods: `.push()`, `.pop()`,
> `.unshift()` and `.shift()` explain what they do, and what they
> return.

> **Question 15**: Are arrays mutable or immutable? Explain your
> answer.

To answer **Question 16**, write the following `for-in` loop in the
JavaScript console to iterate over items in an array:

```
var arr = ["one", "two", "three", "four"];
for (var thing in arr) {
  console.log(thing)
}
```

> **Question 16**: In each iteration of the for loop, is `thing`
> assigned to each _element_ in the array, or each _index_ of the array?

Try the following lines in the JavaScript console and use the
results to answer questions **17** and **18**.

```javascript
var arr = ["one", "two", "three", "four"];
arr.five = 5;
```

> **Question 17**: What are the contents of `arr` now? Is this what you
> expect? What does this imply about JavaScript arrays?

> **Question 18**: What happens when you use a `for-in` loop
> on `arr`? That is, if you ran the following loop:
>
>     var arr = ["one", "two", "three", "four"];
>     arr.five = 5;
>     for (var thing in arr) {
>       console.log(thing)
>     }
>
> What does it print and why?


Prototypes and "classes"
------------------------

While JavaScript is an object-oriented language, its implementation of
objects and "inheritance" is a bit different than in other conventional
object-oriented languages. JavaScript does not have classes in
a traditional sense; instead it relies on sharing properties and methods
with **prototype** objects.

Let's walk through an example. We're going to be defining a JavaScript
class in [three different styles][class-comparison]: [the ES3 style][es3],
[the ES5 style][es5], and [the ES6 style][es6]. The class will be a complex
number (a number composed of both a real and an imaginary part).

[class-comparison]: https://www.webreflection.co.uk/blog/2015/11/07/the-history-of-simulated-classes-in-javascript
[es3]: https://www.webreflection.co.uk/blog/2015/11/07/the-history-of-simulated-classes-in-javascript#the-good-old-es3-way
[es5]: https://www.webreflection.co.uk/blog/2015/11/07/the-history-of-simulated-classes-in-javascript#extending-in-es5
[es6]: https://www.webreflection.co.uk/blog/2015/11/07/the-history-of-simulated-classes-in-javascript#es6-classes

Create a new HTML file called `classes.html` with the following
(non-validating!) contents:

```html
<script src="es3.js"></script>
<script src="es5.js"></script>
<script src="es6.js"></script>
```


### Defining a JavaScript class (the old style)

In this style, you define a **function** that will end up being the
constructor. To define new **properties** on the newly constructed
object, simply assign to `this.<yourPropertyName>`. Write the following
constructor in `es3.js`:

```javascript
function Complex1(real, imag) {
  this.real = real;
  this.imag = imag;
}
```

To define methods, you assign functions to the **prototype** that will
be shared amongst all instances of your "class". You do this *after*
the definition of the constructor.
The methods can refer to properties of the current object by using
`this`. Below the constructor, define a method called `.magnitude()`
that will return the magnitude of the `Complex1` object.

```javascript
Complex1.prototype.magnitude = function() {
  return Math.sqrt(this.real ** 2 + this.imag ** 2);
};
```

Finally, to **instantiate** an object, use the `new` keyword (like Java
and C++). Save `es3.js` and reload "classes.html" in your browser.
Open the JavaScript console and type the following:

```javascript
var c1 = new Complex1(3, 4);
```

Now call its `.magnitude()` method:

```javascript
c1.magnitude();
```

Create a new `Complex1` instance:

```javascript
var c2 = new Complex1(3, 4);
```

Now call this new instance's `.magnitude()` method:

```javascript
c2.magnitude();
```

Try the following lines in the JavaScript console and observe the
results:

```javascript
c1.real === c2.real;
c1.imag === c2.real;
c1 === c2;
c1.magnitude === c2.magnitude;
c1.__proto__ === c2.__proto__;
```

> **Question 19**: What is the value of the `__proto__` property of the
> `c1` and `c2` instances? How did these objects get their `__proto__`
> property?

> **Question 20**: What is the value of `c1.__proto__.constructor`?
> Where was it defined?


### Defining a JavaScript class (the ES5 style)

ECMAScript 5 introduced `Object.create()` that increase the
customization and power given to define classes. However, this is at the
cost at not having an obvious way to define a constructor.

In the file `es5.js`, define a new function called `Complex2` as
follows:

```javascript
function Complex2(real, imag) {
  var obj = Object.create(proto);
  obj.real = real;
  obj.imag = imag;
  return obj;
}
```

Define the prototype object that will be shared by all `Complex2` objects:

```javascript
var proto = {
  magnitude: function() {
    return Math.sqrt(this.real ** 2 + this.imag ** 2);
  }
};
```

Save `es5.js` and reload `classes.html` in your browser. Type the
following to "instantiate" your object:

```javascript
var d1 = Complex2(3, 4);
```

Just as before, try using the `.magnitude()` method:

```javascript
d1.magnitude();
```

Inspect the **prototype** of `d1` by typing:

```javascript
d1.__proto__;
```

> **Question 21**: How does the prototype of `Complex2` objects differ
> from `Complex1`?  Does the behaviour change? Explain your answer.


### Defining a JavaScript class (the ES6 style)

In 2015, the [TC39][] standardized a new style of defining classes, using
the `class` keyword.

[TC39]: https://ecma-international.org/memento/TC39.htm

In the file `es6.js`, define the class called `Complex3` as follows:

```javascript
class Complex3 {
  constructor(real, imag) {
    this.real = real;
    this.imag = imag;
  }

  magnitude() {
    return Math.sqrt(this.real ** 2 + this.imag ** 2);
  }
}
```

Save `es6.js`, and reload `classes.html` in your browser.

In the JavaScript console, instantiate a `Complex3` object using the
`new` keyword:

```javascript
var e1 = new Complex3(3, 4);
```

Yet again, try the `.magnitude()` method of the object you just defined.

```javascript
e1.magnitude();
```

> **Question 22**: How does the prototype of `Complex3` objects differ
> from the prototype shared by `Complex1` objects and the prototype
> shared by `Complex2` objects?  Does the behaviour change? Explain your answer.

To answer Question **23**, type the following in the JavaScript
console:

```javascript
Complex1.prototype = Complex3.prototype;
```

Add a method to the `Complex3` prototype:

```javascript
Complex3.prototype.keepItReal = function () { alert(this.real); };
```

Finally, instantiate an object of the `Complex1` class.

```
var a = new Complex1(3, 4);
```

Try the following the JavaScript console and observe the results:

```javascript
a instanceof Complex1;
a instanceof Complex3;
a.keepItReal();
```

> **Question 23**: Is `a` an instance of the `Complex1` or `Complex3`
> class? Explain.

> **Question 24**: When you added the method `.keepItReal()` to
> `Complex3`, did you use the old style of defining methods or the new
> style? Does this affect its functionality?

---

> **Question 25**: Compare and contrast the three different styles for
> defining classes. Which is easiest to understand? Do they differ in
> behaviour?
