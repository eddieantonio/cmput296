% Lab 4: Introduction to CSS
% CMPUT 296; written by Eddie Antonio Santos
% February 5, 2018

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
`font-style: italic` and `font-family: serif` are
separated by semicolons (`;`).

Apply inline styles to the `<h2>`. Make this element (containing the
artist name, "Yes"), written in Comic Sans MS font, with a white background
colour and magenta text. Adapt the previous examples to help guide you.


> **Question X**: Copy-paste the entire `<h2>` element you just modified
> as the answer to this question. Remember that it must display in your
> browser as magenta Comic Sans MS text on a white background.


Defining styles: CSS syntax
---------------------------

CSS styles are created by writing **rulesets**. A ruleset consists of:

 - a **selector** which selects which elements to apply the styles to.
 - a block of **declarations**. Each declaration sets a **property**
   (like `color`, `font-family`, `margin`, etc.) to a **value** (like
   `white`, `Arial`, `32px`, etc.). Declarations are separated by
   semicolons.

Below is a diagram which explains CSS terminology and syntax with an
example ruleset. This ruleset selects elements with the class
`container` and applies styles to set the colour to `#000` (black) and
to set the size of the font to `24px`:

<p data-height="321" data-theme-id="0" data-slug-hash="NygbJR" data-default-tab="result" data-user="eddieantonio" data-embed-version="2" data-pen-title="CSS Terminology" class="codepen">See the Pen <a href="https://codepen.io/eddieantonio/pen/NygbJR/">CSS Terminology</a> by Eddie Antonio Santos (<a href="https://codepen.io/eddieantonio">@eddieantonio</a>) on <a href="https://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

<aside>
For more information on CSS terminology, see
[this article on CSS-Tricks](https://css-tricks.com/css-ruleset-terminology/).
</aside>

Before continuing, we're going to remove _some_ of the eye-bleeding
styles that were previously applied to the page.

In `styles.css`, append this ruleset to the bottom of the file.

```css
body {
    font-family: inherit;
    background-color: inherit;
    color: inherit;
}
```

Save the CSS file, and reload the page in the browser.

> **Question X**: How many declarations are written in the ruleset for
> `<body>`?

> **Question X**: List the properties in order from the previous
> ruleset. Briefly explain what you think each property affects.

> **Question X**: When you reloaded the page in your browser,
> did you see any changes? Why do you think this is? Hint: look at the
> values that each property is set to in the `<body>` ruleset.

Change the ruleset for `<body>`. Currently, all the values are
`inherit`. You will replace them with the following values: set the
value of `font-family` to `sans-serif`. Set the `background-color` to
`white`. Set the `color` to `black`.

> **Question X**: Copy-paste your updated ruleset for `<body>` as the
> answer to this question. How did the appearance of your webpage
> change?


Selectors
---------

In order to apply styles to an element, we need to know _which_ elements
these styles should be applied to. To *select* particular elements on
a page, we write an appropriate **selector**.


### Element selectors

To select all the elements of a particular kind like `<h1>`, `<p>`, or
`<a>`, simply using the name of the element as the selector, **without
the angle brackets (`<>`)**. For example, the following CSS will show
all the `<p>` tags in 18pt font:

```css
p {
    font-size: 18pt;
}
```

The entire lyrics on this page is in a `<blockquote>` element. The
**User-Agent stylesheet** for most browsers usually apply a margin to
the left and right of the `<blockquote>` element to make it look indented.
However, most of the content in this page _is_ the lyrics, so we'd like
to remove this default margin.

Use an **element** selector to eliminate this default left and right margin.
In `styles.css`, write a ruleset for all `blockquote` elements that will
set the `margin-left` and `margin-right` properties to `0px`. Save your CSS file and
reload the page. The lyrics should no longer be indented.

> **Question X**: Copy-paste your updated ruleset for `<blockquote>` as
> the answer to this question.

> **Question X**: What is a "user-agent stylesheet"? How will it affect
> how your web page will appear in common browsers? Remember to cite
> your sources!


### Class selectors

You can specify one or more classes for an HTML element. This is done by
adding the `class` attribute to the element. For example, in the
following HTML snippet:

```html
<h1 class="song-title"> Yes </h2>
```

The `<h2>` has one class: `song-title`. Some elements have multiple
classes. For example, the first chorus:

```html
<p class="stanza chorus" id="chorus-1">
  I'll be the roundabout<br/>
  ...
</p>
```

This `<p>` tag has two classes: `stanza` and `chorus`. Multiple classes
are specified using only **one** `class` attribute, separating each
class name with spaces.

To write a selector for elements based on class, prepend a period (`.`)
before the class name. For example, to apply a purple text colour to the
elements with the `chorus` class, we would use the following ruleset:

```css
.chorus {
   color: purple;
}
```

---

With the current styles, the instrumental breaks are indistinguishable
from regular lyrics. Instead, we'd like the instrumental breaks

<p style="color:hsl(0,0%,40%);font:italic 1rem sans-serif"> to appear
like this</p>

...such that the text colour is noticeably lighter than the normal text
colour, and is rendered in italics.

All instrumental breaks in the HTML have a class of `instrumental`.
Write the ruleset that will select all the instrumental breaks in the
document and applies these styles (lighter text colour and italic font).

> **Question X**: Copy-paste the ruleset you wrote for the instrumental
> sections as the answer to this question.


### ID selectors

An element on the page can be uniquely identified on the page by giving
it an `id` attribute. For example, the second verse has an `id`
attribute of `verse-2`:

```html
<p class="stanza verse" id="verse-2">
  I will remember you<br/>
  ...
</p>
```

Since IDs are used for the unique identification of a specific element,
**IDs can only be used once on a page**. That is, you can't have
multiple elements on the page with the attribute `id="verse-1"`.
However, you can have multiple elements with IDs on the page; they just
have to be distinct.


To write a selector for an element based on its `id`, prepend a hash (`#`)
before the ID name. For example, to apply a orange text colour to
`verse-2`, we would use the following ruleset:

```css
#verse-2 {
   color: orange;
}
```

---

It would be nice if the bridge of the song was highlighted in some sort
of way. Luckily, the bridge is inside of a `<section>` tag which has its
ID set to `bridge`.

Write a **ruleset** that uses an **ID** selector to style the bridge
`<section>` with a left margin of `1em`, and a smaller font size.

> **Question X**: Copy-paste the **ruleset** you just wrote for the
> bridge section as the answer for this question.

There is a general consensus among web developers to avoid using
IDs in selectors in CSS.

> **Question X**: Search the web for *why* developers discourage the use
> of IDs in selectors. Quote or summarize others' opinions as the answer
> to this question, and remember to cite your sources!

> **Question X**: Write an alternative selector that does **NOT** use
> IDs for the ruleset that applies styles to the bridge section.

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


<!-- margin:; max-width: text-align; -->


Final touches
-------------

There are a few remaining issues on the page. First of all, there is
a magenta border around the content of the page that I would like to get
rid of. Second, I would like the lyrics to **centered**.

### Getting rid of the magenta "border"

There are three properties in CSS that often work in tandem:

 - `padding`
 - `border`
 - `margin`

Do the following procedure to answer the following question.
For each of these properties (`padding`, `border`, `margin`):

 1. Delete any existing declaration of padding, border, or margin in the
    ruleset that applies styles to the `<body>` element.
 2. Add a rule to set the current property (`padding`, `border`, or `margin`) to `0px`.
 3. Save the CSS file, and refresh the page. Did the magenta border go
    away?

> **Question X**: Which property, when set to 0, made the magenta around
> the content disappear? What other effects did setting this property to
> `0px` have?



---

This is the end of the CSS lab; however, we encourage you to play around
with the existing CSS styles, and for you to add more CSS styles.
