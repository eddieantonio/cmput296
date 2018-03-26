% Lab 10: The React web framework
% CMPUT 296; written by Eddie Antonio Santos
% March 26, 2018

Overview
========

 - Learn the basics of React/JSX
 - Create a small interactive React application

Materials
=========

 - An internet connection
 - A modern web browser (like Firefox or Google Chrome)


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**: Questions look like this.

**Remember to cite your sources**.


React
-----

[React][] is a JavaScript front-end web application framework that makes
creating consistent interactive web pages (somewhat) easier than
manipulating the JavaScript DOM directly.

<aside>
The exact revision of the tutorial assumed in this lab is
[538ec13](https://github.com/reactjs/reactjs.org/blob/538ec137440816e19679a49e215ff94dbd8d163e/content/tutorial/tutorial.md).
</aside>

In this lab, we will be following along and doing the exercise in the
[official React tutorial][react-tutorial] and answering some reflection
questions.

Open up the [React tutorial][react-tutorial] in another browser window.
You do not have to complete the entire tutorial to submit this lab. You
will only have to complete the following sections:

 1. What we're building
 2. Prerequisites
 3. How to Follow Along
 4. What is React?
 5. Getting Started
 6. Passing Data Through Props
 7. An Interactive Component
 8. Lifting State Up
 9. Why Immutability Is Important
 10. Functional Components
 11. Taking Turns
 12. Declaring a Winner

You do not have to complete the following sections:

 1. Help, I'm Stuck!
 2. Developer Tools
 3. Storing A History
 4. Showing the Moves
 5. Keys
 6. Implementing Time Travel
 7. Wrapping Up

(You are encouraged to read and complete these sections anyway.)

---

Follow the tutorial up to the section entitled **How to Follow Along**.

How to Follow Along
-------------------

For the purposes of this tutorial, use the first option---open up the
[starter code][] in a new tab, and write your code in the browser.

Continue the tutorial until the section entitled **Developer Tools**.

> **Question 1**: Copy-paste your current version of the `Square` class
> as the answer to this question.

> **Question 2**: Consider the following two lines of JSX:
>
>     <button onClick={() => alert('click')} />
>
> and:
>
>     <button onClick={alert('click')} />
>
> If I want to click on the button and have it `alert()` which of the
> two lines is correct? Why is the other line **incorrect**?

Continue the tutorial from [Lifiting State
Up](https://reactjs.org/tutorial/tutorial.html#lifting-state-up). Stop
when you reach the section entitled **Functional Components**.

> **Question 3**: Copy-paste your code for the `Board` class as the
> answer to this question.

> **Question 4**: From a software maintainability perspective, why is it
> recommend to lift the management of state outside of inner components
> (e.g., from `<Square>` to `<Board>`), having the state to being passed
> down to these components instead?

Continue the tutorial from [Functional
Components](https://reactjs.org/tutorial/tutorial.html#functional-components).
Stop when you reach the section entitled **Declaring a Winner**.

> **Question 5**: Copy-paste your code for the `handleClick()` method of
> the `Board` class as the answer to this question. (This code should be
> update the `squares` array and handle setting 'X' or O').

> **Question 6**: Provide one concise line of code that creates a
> copy of an array in JavaScript. That is every element of `oldArray`
> and `newArray` should be the same, however `newArray === oldArray`
> should evaluate to false. (hint: you should have already written this
> in the `handleClick()` method).

> **Question 7**: What is the time complexity (big-O notation) of
> checking whether two JavaScript Array objects have different elements,
> *if the code always uses arrays in an immutable manner*  (e.g., copies
> the Array before each call to `.push()` or `.shift()`).

Continue the tutorial from [Declaring
a Winner](https://reactjs.org/tutorial/tutorial.html#declaring-a-winner).
Stop when you reach the section entitled **Storing a History**.

> **Question 8**: Copy-paste your code for the `render()` method of the
> `Board` class as the answer to this question.

At this point, you have completed the required sections of the tutorial.
The following questions require you to reflect on your usage of React
thus far.

> **Question 9**: React recommends using JSX---an extension to the
> JavaScript language that is not supported directly by current web
> browsers. What is an advantage of using JSX when writing React
> components (hint: what is the alternative way of writing React
> components *without* JSX?) What is a disadvantage of using JSX in your
> JavaScript projects?

> **Question 10**: Specify two different ways to define new components in
> React. Explain in which situation you would use the first way, and in
> which situation you would use the second way instead.

[react]: https://reactjs.org/
[starter code]: https://codepen.io/gaearon/pen/oWWQNa?editors=0010
[react-tutorial]: https://reactjs.org/tutorial/tutorial.html
[react-tutorial-revision]:
