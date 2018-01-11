% Lab 1: URLs
% CMPUT 296; written Eddie Antonio Santos
% January 8, 2018

Overview
========

 - Investigate URLs by manipulating them manually
 - Learn about the components of a URL
 - Learn about percent-encoding


Materials
=========

 - A modern web browser (like Firefox or Google Chrome)
 - An internet connection


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**. Questions look like this.

**Remember to cite your sources**.


What is a URL?
--------------

A URL (Uniform Resource Locator) is a way to address content on the web.
We will be investigating the components of URL by manipulating the URL
in the **address bar** of your browser of choice.

URLs consist of a series of **components**. In this lab, we will focus
on the following components:

 - **scheme**
 - **host**  (part of the authority)
 - **path**
 - **query**
 - **fragment**

The official [URI standard](https://tools.ietf.org/html/rfc3986#section-1.1.1)
lists more components, but we'll focus on these five components for
now. Only the **scheme** and the **host** are required components of
a URL.

By the end of this lab, you should have a better understanding of the
components of URLs.

> **Question 1**: Consider this URL:
>
>     https://www.ualberta.ca/computing-science/
>
> Using your current understanding of URLs: how many components are in
> this URL? Which components are present (choose from **scheme**,
> **host**, **path**, **query**, and **fragment**)? Provide the value of
> each component. If you are unsure, simply answer "unsure".

Query string
------------

<!--

    https://tools.ietf.org/html/rfc3986#section-3.4

    Note: PRESCRIBES that percent-encoding REQUIRES interpretation as UTF-8.
    https://www.w3.org/TR/REC-html40/interact/forms.html#form-content-type

    It's **here** that it's spaces get converted to +

    The exact structure of query strings is NOT standardized!

    How do HTML forms create query strings?

-->


We will use GitHub's search feature to learn more about the **query
string**.

Go to <https://github.com/search> in your preferred browser.

Search for `linux` (type `linux` in the search box and click "Search").

There should be search results for repositories containing "linux" on
the page.

> **Question 2**: What is the URL now? (copy and paste the URL from your
> browser's address bar as the answer to this question).

> **Question 3**: Describe how the URL has changed from the original URL
> (which was <https://github.com/search>).

Inspect the URL. Find the part that says `q=linux`. Change this to
`q=freebsd` and press enter.

> **Question 4**: Copy-paste your current GitHub search URL here.
> Describe what has changed on the web page and how it relates to the
> URL.

In the web page, on the left-hand sidebar, there should be buttons for
"Repositories", "Code", "Commits", "Issues", "Wikis", and "Users". Make
a note of the current URL. Click on "**Wikis**".

> **Question 5**: What part of the URL changed? How did it change?

These two strings should be present in the URL:

 - `type=Wikis`
 - `q=freebsd`

Swap these two strings in the URL and try it (press enter).

> **Question 6**: Copy-paste the URL you just tried (swapping the two
> strings). Has the web page changed at all? If so, how did it change?

Append `&q=linux` to the end of the URL.

> **Question 7**: Copy-paste the URL you just tried (appending
> `&q=linux`). Has the web page changed at all? If so, how did it
> change?

Append `&type=Users` to the end of the URL.

> **Question 8**: Copy-paste the URL you just tried (appending
> `&type=Users`). Has the web page changed at all? If so, how did it
> change?

The part of the URL you have been changing is called the **query
string**.

> **Question 9**: Reflect on the changes you've made on the URL as
> answers to questions 4, 5, 6, 7, and 8. Describe the purpose of these
> characters in the query string: the question mark (`?`), the ampersand
> (`&`), and the equals sign (`=`). In other words, describe what they
> do in the query string.

Query strings are (by convention
[[1]](https://www.w3.org/TR/REC-html40/interact/forms.html#form-content-type)),
a list of **key-value** pairs.

> **Question 10**: Suppose you were tasked with writing GitHub's search
> feature in Python. What data structure would you use to hold the
> pertinent information in the query string? Pertinent information would
> be the query text, and the type of search (e.g., "Repositories",
> "Code", "Wikis", "Users"), but I might want to add new information in
> the future. Why is this the most appropriate data structure?


The fragment
------------

Go to <http://www.eddieantonio.ca/cmput296/lab-1/>.

You should be greeted by a long, scrolling page of gibberish filler text
(called *lorem ipsum* [[2]](https://en.wikipedia.org/wiki/Lorem_ipsum)).

Make a note of the current URL. Scroll down the page to find the section
heading for "Cupcake". Click on the section heading. You should remain
on the same webpage, but the page may have scrolled. The URL should have
changed.

> **Question 11**: Copy-paste the current value of the URL as the answer
> to this question (Cupcake).

> **Question 12**: What part of the URL has changed?

Now, find the section header for "Bob Ross". Click the section heading.

> **Question 13**: Copy-paste the current value of the URL as the answer
> to this question (Bob Ross).

The part of the URL that has changed is called the *fragment*.
Your browser uses it to refer to different sections *within* a webpage,
as specified by the page's HTML.

> **Question 14**: Create the URL for the section called
> "Hipster". Do this without clicking links in the webpage.


The path and percent encoding
-----------------------------

There are only a few characters allowed anywhere in URLs/URIs.

> Characters that are allowed in a URI but do not have a reserved
> purpose are called unreserved.  These include uppercase and lowercase
> letters, decimal digits, hyphen, period, underscore, and tilde.
>
> <cite>[RFC 3986 §2.3](https://tools.ietf.org/html/rfc3986#section-2.3)</cite>


To represent any other characters, they first need to be
**percent-encoded**. To percent-encode an ASCII character, replace it
with a `%`, and two hexadecimal digits representing the ASCII code of
the character. Here's a small chart of special characters and their
percent-encoding.

| Character    | ASCII code (hexadecimal) | Percent-encoded |
|--------------|-------------------------:|----------------:|
|  (space)     |                       20 |           `%20` |
|  #           |                       23 |           `%23` |
|  +           |                       2B |           `%2B` |
|  :           |                       3A |           `%3A` |
|  ?           |                       3F |           `%3F` |

Consult an [ASCII table](https://en.wikipedia.org/w/index.php?title=ASCII&oldid=819815126#Printable_characters) for more hexadecimal codes.

I have a picture of a cat called `cat.jpg`. Its URL is
<http://www.eddieantonio.ca/cmput296/lab-1/cat.jpg>.
In the same directory, there is a picture of a kitty cat called
`kitty cat.jpg`. Its URL is
<http://www.eddieantonio.ca/cmput296/lab-1/kitty%20cat.jpg>.

> **Question 15**: I have a picture in the same directory called
> `cool cat.jpg`. What is its URL?

> **Question 16**: I have a picture in the same directory called
> `let's cooking.jpg`. What is its URL?

> **Question 17**: I have a picture in the same directory called
> `what's up?.jpg`. What is its URL?

Percent-encoding has been extended to work with UTF-8---a
backwards-compatible extension of ASCII that works with non-English
characters. The way it works is, if a Unicode character is representable
by ASCII, it is percent-encoded the standard way; if the character can
only be represented by UTF-8, then the bytes of its UTF-8 encoding are
encoded (one percent for each byte).

For example, the character `ñ` is used in the Spanish alphabet.
Its Unicode *code point* is **U+00F1**. Encoded in UTF-8, its bytes (in
hexadecimal) are: **C3 B1**. Therefore, a URL with an `ñ` will contain
the sequence `%c3%b1`. For example, I have a picture in that directory
called `buñuelos.jpg`. Its URL is
<http://eddieantonio.ca/cmput296/lab-1/bu%C3%B1uelos.jpg>.

For the following question, use this tool to help you. <http://unicode.scarfboy.com/>

> **Question 18**: I have a picture in the same directory called
> `😹.png`. That cat emoji is **U+1F639**. What is its URL?


Putting it all together
-----------------------

> **Question 19**: Consider the following URL:
>
>     https://en.wikipedia.org/w/index.php?title=Humphrey_the_Whale&oldid=785931250#Humphrey's_journeys_inland
>
> Describe all of the components of this URL: list what components are
> present, and give its value in this URL. Parse the query string, and
> list the key-value pairs.
