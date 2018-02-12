% Lab 4: Introduction to CSS
% CMPUT 296; written by Eddie Antonio Santos
% February 5, 2018

Overview
========

 - ...

Materials
=========

 - ...


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**: Questions look like this.

**Remember to cite your sources**.

Cascading Style Sheets
----------------------

<!-- intro -->

**Tip**: Before answering each question that asks you to write HTML or
CSS code, try it in the files `roundabout.html` and `styles.css`, add
see the change in your browser!

<!-- how to include a css file in your HTML -->

<!--
 Basic syntax:

   https://css-tricks.com/css-ruleset-terminology/
-->


Selectors
---------

<!-- class selectors -->

<!-- element selectors -->

<!-- margin:; max-width: text-align; -->

<!--
   the cascade
-->


### ID selectors

> **Question X**: As the answer for this question, write a **ruleset**
> that uses an **ID** selector to style the bridge `<section>` with
> a **black** background, and a **white** text.

Note that there is a general consensus among web developers to never use
IDs to style elements in CSS.

> **Question X**: Search the web for *why* developers avoid using IDs in
> selectors. Quote or summarize others' opinions as the answer to this
> question, and remember to cite your sources!

If you're not supposed to use IDs to style unique elements on a page,
then what are you supposed to use IDs for?

IDs can be used to link to specific sections on the page. For example,
if I want to link to the Wikipedia page for the University of Alberta,
I would use the following URL:

<samp>https://en.wikipedia.org/w/index.php?title=University_of_Alberta&oldid=821346650</samp>

However, if I wanted to link *specifically* to the "Machine learning and
artificial intelligence" section of that page, I would add
a **fragment** with the **exact text of the ID on the page**. This
section on the  page happens to have an ID of
`Machine_learning_and_artificial_intelligence`, so to URL for that
particular section is:

<samp>https://en.wikipedia.org/w/index.php?title=University_of_Alberta&oldid=821346650<wbr>#Machine_learning_and_artificial_intelligence</samp>

> **Question X**: Create a **relative URL** (without the scheme and
> host) that links to the `bridge` section on the page (The bridge
> starts with the lyrics <q>Along the drifting cloud / the eagle
> searching down on the land</q>).
