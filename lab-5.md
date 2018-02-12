% Lab 4: Introduction to CSS
% CMPUT 296; written by Eddie Antonio Santos
% February 5, 2018

<style

Overview
========

 - Apply CSS styles to an existing HTML document
 - Understand the basic syntax of CSS
 - Be familiarized with common CSS selectors, properties, and values


Materials
=========

 - An internet connection
 - A modern web browser (like Firefox or Google Chrome)
 - A text editor
 - Included files:
   <a href="lab-5/roundabout.html" download><code>roundabout.html</code></a>
   and <a href="lab-5/styles.css" download><code>styles.css</code></a>

Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**: Questions look like this.

**Remember to cite your sources**.


Cascading Style Sheets
----------------------

Cascading Style Sheets (CSS for short) is a language for specifying the
**presentation** of a document. "Presentation" includes how a webpage
will **look** in your browser (colours, fonts, positioning on the page),
but it can also specify how an page will look like when printed, or what
elements a screen-reader should read and in what order, or what
elements to show on a refreshable braille display.

In this lab, we'll be writing **CSS styles** that affect the
presentation of an HTML document. Start by downloading the following two
files to same directory on your computer:

 - The HTML document: <a href="lab-5/roundabout.html" download><code>roundabout.html</code></a>
 - The stylesheet: <a href="lab-5/styles.css" download><code>styles.css</code></a>

**Tip**: Before answering each question that asks you to write HTML or
CSS code, try it in the files `roundabout.html` and `styles.css`, add
see the change in your browser!


Including styles from an external CSS file
------------------------------------------

`styles.css` already contains one **ruleset** that will be applied to
the entire HTML document. However, the HTML document must first **link**
to the CSS file to use its styles.

Open `roundabout.html` in your browser. You will probably see a boring
page, with a default background (usually white), default text colour
(usually black), and the default font (usually Times New Roman).

`styles.css` contains some conspicuous styling choices. In order to
view the results of `styles.css`, we must **link** to it.
Within the `<head>` element of `roundabout.html`, add a `<link>` element
to apply the CSS file `styles.html` to the page.

A `<link>` element for including an external CSS file has this basic
syntax:

```html
<link rel="stylesheet" href="path/to/file.css" />
```

Adapt the example above to apply the styles within `styles.css` to
`roundabout.html`. Replace `path/to/file.css` with the relative or
absolute URL as needed. The `<link>` element must be a child of the
`<head>` tag. `<link>` tags are typically placed near the end of the
`<head>` element, after the `<meta>` and `<title>` elements. Add the
appropriate `<link>` element, save the HTML file, and reload the page.

If you have done this correctly, the page should appear magenta, with
the text written in Comic Sans or some other "fantasy" typeface.

> **Question X**:  Copy and paste the entire `<head>` element from
> `roundabout.html` (including the `<link>` you just added) as the
> answer to this question.


[link]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link


Defining styles within an HTML document
---------------------------------------

In simplified terms, the "Cascading" in "Cascading Style Sheets" means
that styles are inherited (they "cascade down", like a waterfall),
unless something **closer** or **more specific** applies to it.

To define styles directly in an HTML document, there are two ways: using
a `<style>` element, or using the `style` attribute of elements.

Add the following `<style>` element to the end of the `<head>` in
`roundabout.html`:

```html
<style>
header {
   font-family: Helvetica, Arial, sans-serif;
   color: black;
   background-color: white;
}
</style>
```

Save the HTML file, and reload the page in your browser.

> **Question X**:  Describe what changed in your browser after you added
> the `<style>` element?

You may apply CSS styles to individual elements using the `style`
attribute. These are called *inline styles*. Inline styles are applied
by simply adding a `style` attribute to any element, like so:

```html
<p style="color: pink; font-style: italic; font-family: serif">
   I will be a pink paragraph, in italic serif font.
</p>
```

Which will display as:

<p style="color: pink; font-style: italic; font-family: serif">
   I will be a pink paragraph, in italic serif font.
</p>

Notice how **property/value pairs** like `color: pink` and
`font-style: italic` and `font-family: Times New Roman, serif` are
separated by semicolons (`;`).

Apply inline styles to the `<h2>`. Make this element (containing the
artist name, "Yes"), written in Comic Sans MS font, with a white background
colour and magenta text. Adapt the previous examples to help guide you.


> **Question X**: Copy-paste the entire `<h2>` element you just modified
> as the answer to this question. Remember that it must display in your
> browser as magenta Comic Sans MS text on a white background.




CSS syntax
----------

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
