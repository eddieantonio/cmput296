% Lab 4: Introduction to HTML
% CMPUT 296; written by Eddie Antonio Santos
% February 5, 2018

Overview
========

 - ...

Materials
=========

 - An internet connection
 - A modern web browser (like Firefox or  Google Chrome)
 - A text editor (with good Unicode support!)


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**: Questions look like this.

**Remember to cite your sources**.

# What is HTML?

The **Hypertext Markup Language** defines the structure and content of
a webpage. In this lab, we'll modify some small HTML documents
to get a better understanding of the structure of HTML.

Quick HTML syntax refresher
---------------------------

<aside>
Note that while this lab pedantically distinguishes between the terms
**element** and **tag** (as per the [WhatWG][] standard), in common
discussion, you may hear people use these terms interchangeably such as
"Write a new `<a>` tag in your document" when they really mean "`<a>`
element". This is so common, your instructors may often mix these terms
up without realizing!
</aside>

[WhatWG]: https://html.spec.whatwg.org/multipage/introduction.html#a-quick-introduction-to-html

HTML is made up of nested **elements**, which are marked by a **start
tag**:

    <tag>

and terminated by an **end tag**:

    </tag>

Elements are often **nested**. Consider the following example:

    <html>
      <head>
        <title> </title>
      </head>
      <body>
      </body>
    </html>

In this example, the **root element** is `<html>`; `<html>` has two
**children** elements: `<head>` and `<body>`. Finally, `<head>` contains
one child element: `<title>`. The `<head>` and
`<body>` elements are **siblings**.

For questions 1 and 2, consider the following example:

    <body>
      <p> Hello, <strong>World</strong> </p>
    </body>


> **Question 1**: What element is the child of the `<body>` tag>?

> **Question 2**: Does the `<p>` tag have any child elements? If so,
> what are they?

Attributes
----------

HTML elements may have **attributes**. Attributes are defined **only**
in the start tag:

    <tag attribute-1="value 1" attribute-2="value 2">
      ... contents ...
    </tag>


Attributes are a way of specifying name/value pairs attached an element.
Most of these name/value pairs are optional.

The "HT" in "HTML" stands for "Hypertext" which is the nature in which
different HTML documents can be linked together with *hyperlinks*. To
make a *hyperlink* in an HTML document, one must use an `<a>` element,
whose start and end tag surround the desired link text. The `<a>`
element **requires** the `href=` attribute ("href" is short for "hyperlink
reference"), which specifies the URL which clicking the link will go to.
For example, here is a link to the homepage of `ualberta.ca` with the
clickable text being "University of Alberta homepage"

    <a href="https://ualberta.ca/">
      University of Alberta homepage
    </a>

This link will look like this: <a href="https://ualberta.ca/">
University of Alberta homepage</a>.

> **Question 3**: Provide the HTML code for a link whose link text is
> "Example domain" and clicking it will go to `http://example.com/`.

> **Question 4**: Why is the `href=` attribute required for the `<a>`
> element? Try to answer this question without consulting external
> resources.



Self-closing tags
-----------------



<!-- what part does modifying <title> affect? -->
<!-- what part does modifying <h1> affect? -->


```html
<!DOCTYPE HTML>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Hello, World!</title>
      <link rel="stylesheet" href="...">
   </head>
   <body>
      <h1>Hello, World!</h1>
      <p>
        Listed in descending order of top 5 languages by number of
        speakers.
        <a href="https://www.ethnologue.com/statistics/size">
          [Source]
        </a>
      </p>

      <ol>
        <li lang="zh">你好，世界</li>
        <li lang="es">¡Hola, Mundo!</li>
        <li lang="en">Hello, World!</li>
        <li lang="ar"><span dir="rtl">مرحبا بالعالم!</span></li>
        <li lang="hi">नमस्ते दुनिया</li>
      </ol>
   </body>
</html>
```

<!-- give mini syntax lessons -->

<!-- how many children of the <body> tag? -->

<!-- attributes and ids:

 1. take earlier lorem ipsum page and download it.
 2. add ids to it to make it scroll.
 3. copy the lines changed as the answer

-->

# `<meta charset="...">`

<!--
Assume they already know attributes by here.

-->

Copy the above example to and paste it into a new text file (use your
favourite text editor). Save that text file as `example.html`. Now open
that file from your file manager. It should open in your default
browser and display something like this:

<!-- screenshot of intended rendering: -->

<!-- download link for this page. -->

![The rendered page in my browser](lab-4/example.html.png)

> **Question 1**: When this page opened in your browser, did it use
> HTTP? Provide evidence for your answer (hint: look at the URL).

<!--
 Encodings list:
  - US-ASCII
  - GB-18030
  - GB-2312
  - ISO-8859-1
  - CP1250
  - KOI cyrillic encoding
  - Shift-JIS
-->

<!-- render without meta charset line -->
<!-- render trying different encodings -->
<!-- why is UTF-8 the only possible encoding for the characters on this
     page? this questino will be difficult to word...

     Say I'm saving this file, and the text editor is asking me what
     character encoding to use. Why is UTF-8 the only possible 8-bit
     encoding to use?
     -->

<!-- Question involving messing around with meta tags -->

<!-- Question involving <title> tag: stuff in body is the content in the
     viewport. -->

<!-- Question involving changing CSS styles -->

<!-- Question involving creating an <a href="..."> -->

<!-- Question involving creating an <img src="..." alt="..."> -->

<!-- QUESTION INVOLVING FILE ENCODINGS! -->

<!-- teach them importance of escape chars: &lt; &gt; &amp; -->

<!-- teach them what an HTML comment is! -->

<!-- teach them to inspect with the dev tools -->

<!-- eventually get them to produce this: -->

<!-- use this as inspiration:
   http://ladieslearningcode.github.io/llc-html-css-one-page/slides.html#slide7
   http://ladieslearningcode.github.io/llc-html-css-one-page/slides.html#slide22
-->
