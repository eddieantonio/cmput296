% Lab 11: Web security: Cross-site scripting
% CMPUT 296; written by Eddie Antonio Santos
% April 2, 2018

Overview
========

 - Learn what a cross-site scripting attack is
 - Exploit some cross-site scripting vulnerabilities
 - Reflect on how to prevent cross-site scripting vulnerabilities

Materials
=========

 - An internet connection
 - A modern web browser (like Firefox or Google Chrome)


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**: Questions look like this.

**Remember to cite your sources**.


Introduction
------------

**Cross-site scripting** is the act of inserting (possibly malicious)
JavaScript code into a different website when it is not intended.
Typically this is to extract sensitive information from unsuspecting
users (such as `document.cookie`), which may provide a way for an
attacker to gain access to users' accounts without a password.

In this lab, you will be writing code that performs cross-site scripting
attacks on vulnerable webpages (fake webpages, specifically constructed
to help teach cross-site scripting!). You will also offer solutions on how
to write websites that are immune to these attacks.

To start cross-site scripting, go to this site:
<https://xss-game.appspot.com/>. Read the introduction, and proceed to
**level 1**. Then continue reading this write-up.


Level 1
-------

The goal is to insert the HTML `<script>alert('CMPUT 296')</script>` into
the embedded web page, a fake search engine called "FourOrFour".

![Vulnerable webpage, embedded in
<https://xss-game.appspot.com/level1>](./lab-11/vulnerable.png)

Although you have read-only access to the web server's source code, you
do not have access to modify it; in order to insert your code, you'll
have to find a way to *trick* the website into executing your code!
The first thing to try is to **insert your code** into a source of input
in the webpage, that is otherwise intended for normal user interactions.

Consider the sources of input on the page: there are at
least two sources of input.

> **Question X**: List as many sources of input on the homepage of
> "FourOrFour". Hint: look both inside the viewport and *outside* of the
> viewport.

Try simply providing `<script>alert('CMPUT 296')</script>` into any sources
of input into the vulnerable page. Feel free to use the **hints** at the
bottom of the page.

If you did this right, the page should pop up a box saying "CMPUT 296", and
the game should allow you to proceed to the next level.

> **Question X**: What source of input did you use to make the page do
> the `alert('CMPUT 296')`?

Toggle the "Target code" on the page. This is the Python source code for
the server.

> **Question X**: What part of the source code was responsible for
> allowing you to execute your own `<script>` on the page? Why is it
> vulnerable to the cross-site scripting attack (in other words, why
> does it allow you to insert _your_ code into the webpage).

Once you have succeeded in exploiting level 1, proceed to level 2.


Level 2
-------

In this level, simply inserting a `<script>` element into the page will
not work. You must try some other way of exploiting the input sources on
the page. Once again, identify the input sources, and try getting your
code into the page. The goal, as before, is to get the page to execute
`alert('CMPUT 296')`.

Fun fact! The `onclick` attribute is not the only attribute that will
execute JavaScript on an arbitrary HTML element. For example, there's
the `onerror` attribute. You can add this attribute to a "media" HTML
element (`<img>`, `<video>`, `<audio>` tags) and it will run the code
when there's some kind of error (e.g., when the image specified fails to
load due to a 404 error).

```html
<img src="http://example.com/space-cats-in-space.jpg"
     onerror="console.log('sorry, could not load space cats')">
```

<img src="http://example.com/space-cats-in-space.jpg" onerror="console.log('sorry, could not load space cats')">

> **Question X**: Copy-paste the input your provided that to pass
> **Level 2** as the answer to this question.

> **Question X**: Why did the exploit that you just wrote work? If you
> were writing a chat page like the vulnerable "Madchattr" webpage, how
> would you program it to make such an exploit impossible?

Once you have succeeded in exploiting level 2, proceed to level 3.


Level 3
-------

In order to insert malicious code (HTML, or [SQL][bobby]) into a webpage, you
may first have to complete existing code that is being generated such
that it is syntactically-valid. Thus, the attacker (you, in this
example) can insert the malicious code, after the completed,
syntactically-valid code.

[bobby]: https://xkcd.com/327/

> **Question X**: What code do you need to complete the following
> `<img>` tag to make it syntactically-valid?
>
>     <img href="/static/images/images.jpg

A thing to be careful about when writing user-facing code are any places
where you are concatenating many strings together to form valid code
(e.g., HTML).

> **Question X**: Toggle the code open, and view the code for
> `index.html`. Identify the line numbers of JavaScript where user input
> is being concatenated with strings to create HTML code.

Using what you learned in the past two questions, create an exploit that
will execute `alert('CMPUT 296')` into the "cloudiddly" web page. You
may find [this percent-encoding
app](https://meyerweb.com/eric/tools/dencoder/) helpful to insert your
malicious code.

> **Question X**: Copy-paste the exploit your wrote to pass **Level 3**
> as the answer to this question.

Once you have succeeded in exploiting level 3, proceed to level 4.


Level 4
-------

One way that people have tried to prevent XSS attacks is to escape **HTML
tags** before creating the page. Level 4's "timemer" app tries to do
this. Basically, before creating HTML, the following transformations are
made:

 - `<` is converted to `&lt;`
 - `>` is converted to `&gt;`
 - `&` is converted to `&amp;`
 - `'` is converted to `&#39;`

 This is so that you cannot insert arbitrary HTML tags into webpages
 (e.g., you cannot insert a `<script>` element, or even a `<img>`
 element).

Despite the HTML escaping, "timemer" does something unwise with user
input.

> **Question X**: Toggle the code open, and view the code for
> `timer.html`. This is a *template* in which any mention of
`{{ timer }}` is replaced with the user input with HTML tags
> escaped. Identify the line numbers tags where `{{ timer }}` is mentioned.

> **Question X**: Run the following in the JavaScript developer console:
>
>     console.log('hello ' + alert('goodbye') + ' world');
>
> Describe what is output (either as a pop-up window or in the
> console). Why does the output appear in this order?


> **Question X**: Copy-paste the exploit your wrote to pass **Level 4**
> as the answer to this question. Where did you insert this input?

Once you have succeeded in exploiting level 4, proceed to level 5.


Level 5
-------

You are aware of the `http://` and `https://` URI schemes, but there are
many more. For example,

 - `mailto:` allows you to instruct the browser to send an email when
   the link is clicked.
 - `data:` allows to specify arbitrary data in HTML and CSS documents.
   This is useful for embedding an images into one HTML file without any
   external resources.
 - `javascript:` allows you to run JavaScript when a link is clicked.

> **Question X**: Toggle the code open, and view the code for
> HTML templates. Identify both the file and the line number where
> `{{ next }}` appears as the `href` attribute of a link.

> **Question X**: Toggle the code open, and view the code for
> `level.py`. How does the server check whether the user requested the
> "signup", "confirm", or "welcome" page? (Hint: describe the `if/elif`
> block that deals with signup/confirm).

> **Question X**: Copy-paste the exploit your wrote to pass **Level 5**
> as the answer to this question. Where did you insert this input? How
> would an unsuspecting user trigger it?

Once you have succeeded in exploiting level 5, you _may_ attempt
level 6. However, it requires being able to create external resources,
so it is not required for this lab.

---


> **Question X**: Using your own words, describe what XSS is. If you use
> external sources to define XSS, you must not only cite your sources
> but you must also rewrite what the source says in your own words.

> **Question X**: Using what you learned in this lab, provide a general
> suggestion for how to program web applications that are NOT vulnerable
> to XSS attacks (like the ones you exploited in this lab).
