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
 - ...


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**: Questions look like this.

**Remember to cite your sources**.


Introduction
------------

**Cross-site scripting** is the act of inserting (possibly malicious)
JavaScript code into a different website when it is not intended. You,
Typically this is to extract sensitive information from unsuspecting
users (such as `document.cookie`), which may provide a way for an
attacker to gain access to users' accounts without a password.

In this lab, you will be writing code that performs cross-site scripting
attacks on vulnerable webpages---fake webpages, specifically constructed
to help teach cross-site scripting! You will also offer solutions on how
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
least two sources of input!

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


Level 3
-------


---

> **Question X**: Using your own words, describe XSS If you use sources
> to define XSS, you must cite your sources and you must rewrite what
> the source says in your own words.
