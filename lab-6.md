% Lab 6: Writing HTML & CSS from scratch
% CMPUT 296; written by Eddie Antonio Santos
% February 26, 2018

Overview
========

 - Create an HTML and CSS page from scratch
 - Create a form to GET information from an external resource


Materials
=========

 - A modern web browser (like Firefox or Google Chrome)
 - An internet connection
 - A text editor

Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**. Questions look like this.

**Remember to cite your sources**.


Creating an band fan site from scratch using HTML and CSS
---------------------------------------------------------

In the first part of this lab, we'll be creating a fan site for your
favourite musical group (e.g., Evanescence, Girls' Generation, Maximum
the Hormone, Opeth, Spice Girls, etc.). If you don't have a favourite
band, make a [BTS][] fan site (the particular band doesn't matter).

We'll be writing this site from **scratch**. This means no use of site
generators, themes, Bootstrap, or any pre-written code. **Try as much as
possible to not copy-paste any code from the internet**. All the code
you'll write in your text editor should be typed out by hand (even if
you had to go consult the internet on how to do something in HTML and
CSS). There are only two exceptions to this recommendation: links like
<span style="text-overflow:ellipsis;display:inline-block;max-width:100%;white-space:nowrap;overflow:hidden;">https://upload.wikimedia.org/wikipedia/commons/c/ca/%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8%28BTS%29_180110_%EC%A0%9C_32%ED%9A%8C_%EA%B3%A8%EB%93%A0%EB%94%94%EC%8A%A4%ED%81%AC.png</span>
are okay to copy-paste; [lorem ipsum][] text is also okay to copy-paste.
You will also be required to copy-paste the code _you_ have written as answers to
many questions in this lab.

[BTS]: https://en.wikipedia.org/wiki/BTS_(band)
[lorem ipsum]: https://www.webpagefx.com/tools/lorem-ipsum-generator/

Create the scaffolding
======================

Create a new text file called `index.html`. Inside this text file, type
the minimal HTML required for a valid HTML 5 page. You can find an
example in [your
notes](http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/3).
Verify that this is valid HTML 5 by copy-paste the code you wrote into
the [W3C validator](https://validator.w3.org/#validate_by_input).

![Pasting my code into the validator.](./lab-6/paste-into-validator.png)

![My HTML passed withour errors or warnings.](./lab-6/validate-pass.png)

Do not continue until your minimal HTML passes the validator with
0 errors.

> **Question 1**. Copy-paste your minimal HTML (that passes the W3C
> validator) as the answer to this question.

<!--

write html from scratch

Make sure it is valid HTML 5. Use the validator: http://validator.w3.org/ http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/3

 - Will have at least an <h1>.

 - <p> http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/9

 - <figure> and <figcaption> [NEW] https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption
 - <img> http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/13 attribute the work
 - make it float to the right of the content. give it some margin to put some space between it an the text. [NEW]
 - <a> http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/14
 - Use a <span> to apply inline styles http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/17
 - apply display: inline-block;
 - Maybe like a transform: rotate(12deg);
 - What happens when you remove display: inline-block from this span?
   Why does this happen?

 - <footer> at bottom
 - Use an HTML entity to add a copyright symbol to the bottom. [ NEW]
 - Use a font-size smaller to the footer.

 - A custom hyperlink style with :hover http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/32

 - Fancy Captital Letter for the first item of a paragraph WITHOUT modifying the HTML. Show the CSS. http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/32

---

<form action="http://localhost:8000/"> http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/38
<select> http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/42
   OR <input type="radio"> http://webdocs.cs.ualberta.ca/~hindle1/2014/HTML-Slides/#/41

<form>

inspect element

resizing image with CSS width: height:


-->
