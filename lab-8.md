% Lab 8: Asynchronous JavaScript and XMLHttpRequest (AJAX)
% CMPUT 296; written by Eddie Antonio Santos
% March 18, 2018

Overview
========

 - Learn about asynchronous programming in JavaScript
 - Learn the API for `XMLHttpRequest`
 - Perform asynchronous DOM manipulation

Materials
=========

 - Google Chrome's [DevTools]
 - An internet connection
 - A text editor
 - A Python 3.5+ interpreter that can be run from the command line.
 - Included files:
   <a href="lab-8/server.py" download><code>server.py</code></a>,
   <a href="lab-8/index.html" download><code>index.html</code></a>

[DevTools]: https://developer.chrome.com/devtools


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**. Questions look like this.

**Remember to cite your sources**.

<!-- goal: make a valid XHR. Put it in a <div> -->


AJAX
----

In this lab, the goal is to make a request to an external server
and show the results in the webpage **without** navigating away from the
current webpage.


### Warm-up exercise: DOM manipulation

**DOM Manipulation** refers to using JavaScript to change the **Document
Object Model (DOM)**, which represents the logical structure of your
HTML document loaded in the web browser.

This means that we can access and modify the text and elements on the
webpage. The language we'll use to do this is JavaScript.

<aside>
Just as in [Lab 6](./lab-6.html),
if you are security conscious, you should verify that the SHA-256
checksum of `server.py` that you downloaded matches the checksum that
I computed:

```
334e487a26471a1724d22da4b5418efba63ad2a0b1eb269cf5e989bf3be08058
```

Use [`sha256sum`](https://help.ubuntu.com/community/HowToSHA256SUM) to verify that the file you downloaded has the same
SHA-256 checksum. Please peruse the source code to ensure it is not malicious in nature.
</aside>


Please download
<a href="lab-8/server.py" download><code>server.py</code></a> and
<a href="lab-8/index.html" download><code>index.html</code></a>.
Place these files in the same directory.

Now, open up a terminal and navigate to the directory in which you
downloaded the files. Start the server by typing:

```sh
python3 server.py
```

Look at the source code of the provided file called `index.html`.

> **Question 1**: How many elements in `index.html` have an `id`
> attribute? What are these elements, and what are the IDs?

Open up the [DevTools JavaScript Console][console]
(Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>;
macOS: <kbd>Cmd</kbd> + <kbd>Alt</kbd> + <kbd>J</kbd>).

[console]: https://developers.google.com/web/tools/chrome-devtools/console/?hl=en

We're going to programmatically retrieve the text of the `<h1>`
displaying the title of the page.

In the JavaScript console, type:

```javascript
var h1 = document.getElementById('main-title')
```

We just created a variable called `h1`.


> **Question 2**: Retrieve the value of `h1` by typing `h1` in the
> console. What kind of output do you get? What does
> `document.getElementById()` do?

Now type this in the console:

```javascript
h1.innerText
```

> **Question 3**: What did this line return?
> What type of JavaScript value/object did this return?
> Where did this value come from?

<a id="innerText"></a>

Now, assign to `h1.innerText`. Type the following, replacing
"`<name>`" with your name:

```javascript
h1.innerText = "<name>'s AJAX Calculator"
```

> **Question 4**: What has changed on the webpage? Describe why the
> previous lines of code had this effect.

Now, type code in the JavaScript console to change the text on the page
for the `<output id="the-answer">` element to `No answer yet`.

> **Question 5**: Copy-paste the JavaScript code you just wrote to
> change the `<output>` element as the answer to this question.


Asynchronous programming
------------------------

To recap, the goal of this lab is to make a request to an external
server and display a result without navigating away from the current
webpage.

In order to do this, it is vital to understand **asynchronous
programming**.


### What is "asynchronous programming"?

In typical procedural programming, the programmer is often in control of
the exact flow of instructions. That is, you, as the programmer say:

```js
if (x < 0) {
  return 0;
}
```

And the program will _immediately_ test if `x` is indeed less than 0,
and then it will execute the consequent as soon as it determines this.

Similarly, if you write JavaScript code that says:

```js
add(2, 2)
```

The program will call the `add()` function _immediately_.

However, you, as a programmer, have no control over user interaction, or
at what moment, exactly, an external server replies to you (if at all).
For example, the developers of Facebook Messenger have no control if
or when a user will write a message to someone and send it. Yet, the
developers of Facebook want you to be able to send a message at _any
moment_ without navigating away from the page. This is an example of an
_asynchronous event_. "Asynchronous" means that the event may not be
initiated by your action, as a programmer. Rather, an external event
may initiate an action at any moment, and you, as a programmer, must
declare a way to respond to that event.


### Asynchronous programming in JavaScript

We're going to register an **event listener** that will be called whenever
some event occurs on the page. Registering event listeners is how we
write asynchronous code in JavaScript. Essentially, we register some
code that will run _when_ a certain event occurs.

Open up `index.html` in your text editor of choice. Near the bottom of
the file should be a `<script></script>` element. We will write
JavaScript code within this element.

<a id="submit"></a>

Create an event listener that will listen to the "submit" event for the
form.

First, write some code that assigns a reference to the
`<form id="input-form">` element to a variable called `form`, like this:

```javascript
var form = /* write your code here */;
```

A `<form>` is an
[`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget).
This means we can call `.addEventListener()` to register a function to be
called when a certain event occurs.

At the end of the `<script>` element, write this:

```javascript
form.addEventListener('submit', function (event) {
  alert("Form submitted!");
});
```

Reload <http://localhost:8000/> in your web browser.
Open up the JavaScript console and ensure there are no errors
in your code. Once you're sure your code has no errors,
fill out the form as you wish, and click "Calculate".

> **Question 6**: When does the function you just wrote get called?
> How many arguments does this function take?
> Does this function have a name?

> **Question 7**: Describe what happens when you press the "Calculate"
> button. After you dismiss the message, does the browser stay on the
> same webpage or does your browser navigate to a different webpage?

Add a line to your `submit` event handler.

Somewhere in the body of the function you just defined, add this code:

```javascript
  event.preventDefault();
```

Reload <http://localhost:8000/>, fill out the form, and press submit
again.

> **Question 8**: What happens when you press "Calculate" now? What
> does `event.preventDefault()` do? What is the "default" that it is
> preventing?


### `XMLHttpRequest`

<aside>
Despite its name, you can request *anything* using
`XMLHttpRequest`---not just XML.
</aside>

The `XMLHttpRequest` object allows us to make an arbitrary HTTP request
using JavaScript. In order to do this we must first:

 * Instantiate a new `XMLHttpRequest` object.
 * "Open" a new request, specifying the request method, the request URI,
   and whether we want the request to be asynchronous or not.
 * Assign event handlers to be called at different stages of processing
   the HTTP response.
 * Send the HTTP request.

Open the DevTools JavaScript console. We will experiment with the
`XMLHttpRequest` object.

<a id="xhr"></a>

In the console, instantiate a new `XMLHttpRequest` object and assign it
to a variable called `xhr`.

<!-- screenshot? -->

```javascript
var xhr = new XMLHttpRequest();
```

We want to execute an asynchronous GET request to
<http://localhost:8000/calc/>.
Use the documentation on
[XMLHttpRequest.open](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/open)
to write the appropriate code for this. Test your code in the console to
ensure it does not crash.

> **Question 9**: Copy-paste the working code you wrote to make a `GET`
> request to <http://localhost:8000/calc/> as the answer to this
> question.

Now, define your **event handler**. To do so, you must assign a function
to `xhr.onload`.

Assign the following event handler:

```javascript
xhr.onload = function () {
  alert(xhr.responseText);
};
```

> **Question 10**: The way we defined an event handler for the `submit`
> event earlier and the way we defined an event handler for when the
> XMLHttpRequest is loaded has different syntax. Explain what is
> semantically different about how we defined these two event handlers.

> **Question 11**: What part of the HTTP response will be contained in
> `xhr.responseText`? Be as descriptive as possible using terms used
> when messages in the HTTP protocol.

Now that we have opened the request with the desired HTTP method and
request URI, and setup what will be called when the we receive the full
HTTP response, we can finally send the HTTP request. Write the following
code in the console:

```javascript
xhr.send();
```

> **Question 12**: What is shown in the pop-up message after calling
> `xhr.send()`? Do you get any error messages? What was the HTTP status
> code of the GET request to <http://localhost:8000/calc/>? Describe
> what this error message means.


### Getting parameters from the webpage

<a id="params"></a>

AJAX requests typically require sending parameters to the server.
Since this is a `GET` request, we'll have to package up the parameters
in the URL's query string.

<http://localhost:8000/calc/> expects three query parameters:

 - `a` --- a number
 - `b` --- a number
 - `op` --- a value in `+`, `-`, `*`, or `/`

We can obtain this from the `<form>` on the page. With the latest
version of <http://localhost:8000/> open in you browser, open the
JavaScript console and get a reference to the `<form>` element and
assign it to a variable called `form`.

```javascript
var form = /* write your code here */;
```

Now type the following in the console:

```javascript
form.elements["a"]
```

Then type:

```javascript
form.elements["op"]
```

Now try the next two lines:

```javascript
form.elements["a"].value
```

```javascript
form.elements["op"].value
```

> **Question 12**: What do these previous lines return? Where do the
> values come from? Use the drop-down on the webpage to change the
> operation (`+`, `-`, `*`, `/`). Now what does
> `form.elements["op"].value` return?

We must construct an appropriate query string that sends the parameters
`a`, `b`, and `op` to make a valid request to
<http://localhost:8000/calc/>.
Use the following template to get started. Set the values of `a`, `b`,
and `op`, to the values obtained from the `<form>` element.
Use [encodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
to do percent-encoding where appropriate.

```javascript
var url = "http://localhost:8000/calc/";

url = url + /* write your code here */;
```

> **Question 13**: What's the difference between
>
>     "&op" + form.elements["op"].value;
>
> and
>
>     "&op" + encodeURIComponent(form.elements["op"].value);
>
> Which one is correct? Why is the other option *incorrect*?

> **Question 14**: Copy-paste your code that constructs the valid URL as
> the answer to this question.

Once you have created a valid URL, create a new `XMLHttpRequest` object
as before, but this time, open the URL you just created with a valid
query string, and set an `onload` event handler that prints the
`xhr.responseText` ([see above](#xhr) for a refresher on how we did
this).
With the `XMLHttpRequest` object set up to request to the correct URL,
execute `xhr.send()`.

> **Question 15**: Executing `xhr.send()` should now allow us to receive
> an HTTP response with status code 200. Now that the correct URL has
> been sent, what is the value of the `xhr.responseText`?

> **Question 16**: Use the **Network** panel to inspect the successful
> HTTP response to <http://localhost:8000/calc/> (with status code 200).
> What is the `Content-Type` of this response?


Putting it all together
-----------------------

We're going to combine

 - [registering an event listener for submit events](#submit);
 - [getting form values from the page](#params);
 - [sending an `XMLHttpResponse`](#xhr); and
 - [changing an element's `.innerText`](#innerText)

 to create our AJAX-powered calculator. By the end of this, the answer
 should appear in the same webpage without navigating away from the
 current page.

Open `index.html`, and write your JavaScript code to the `<script>`
element near the bottom of the file.

Define an event listener to the `<form>` element. It should prevent the default
action, which is to navigate away from the page. If there already is an
event listener defined in your copy of `index.html`, delete it and write
a new one.

**Within** the event handler, use `form.elements[...]` and
`encodeURIComponent()` to construct
a URL to be sent to <http://localhost:8000/calc/> with query parameters
based on what's typed and selected within the webpage.

Create an `XMLHttpResponse` object and assign it to the variable name
`xhr`, and open a `GET` request to the URL you just constructed. Assign
a new `onload` handler. Within the `onload` handler, get a reference to
the `<output>` element. Now, change the `<output>` element's text to the
value of `xhr.responseText`.

Finally, still within the "submit" event listener, call `xhr.send()` to
start the HTTP request.

Save your changes to `index.html` and reload <http://localhost:8000/>.
Enter in some values on the form and click `Calculate`. If you have done
everything right, it should display the answer on the same page, without
navigating to a new page.

> **Question 17**: Copy-paste the JavaScript you wrote within the
> `<script>` element as the answer to this question. Make sure it
> successfully performs an HTTP request and changes the content of the
> `<output>` element.
