% Lab 3: HTTP from scratch
% CMPUT 296; written by Eddie Antonio Santos
% January 29, 2018

Overview
========

 - Learn how to create a TCP connection on the command line
 - Use the TCP connection to backwards-engineer an HTTP request
 - Create our own HTTP request using a text editor

Materials
=========

 - An internet connection
 - A modern web browser (like Firefox or  Google Chrome)
 - Unix command line tools: `dig`, `nc` (netcat), `tee`, `xxd`
 - A text editor


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**. Questions look like this.

**Remember to cite your sources**.

--

In last week's lab, we spied on how your browser creates HTTP requests
to communicated with an HTTP server. In this lab, we will be creating
HTTP requests "from scratch" using nothing but an open TCP connection.


Creating a TCP connection
-------------------------

In order for your computer to be able to retrieve this cat meme using
HTTP:

![Picture of a cat, attempting to sit in a tiny, tiny box. Caption
reads: "413: Request entity too large"](./lab-3/cat-meme.jpg)

...it first must establish a TCP connection with the server hosting the cat
meme. Once a TCP connection is established, the client and server can
communicate with each other using HTTP requests/responses, written as
ASCII text.

Other CMPUT courses will cover how the network layers up to TCP/IP work;
however, in this course, we can use the `netcat` program to establish
fresh TCP connections; either as a client to a server, or as a server
ourselves.

We will create a process to **listen** to TCP connections. This will be
our server. To do this, do the following in the command line:

    nc -l 8000

You have established a new TCP server, listening on **port 8000** for new
connections.

To test this, open a new terminal, and connect to your server by
invoking:

    nc 127.0.0.1 8000

This command means, connect to the computer with IP address `127.0.0.1`,
and connect to port 8000 (as a client).

> **Question 1**. What computer does 127.0.0.1 refer to?

Now, with both terminals running `nc` on your screen, type something
into one of the terminals, and press <kbd>Enter</kbd>. If all went well,
you should be seeing the text appear in the other terminal.
Congratulations! You just used TCP to send a message from one process to
another process!

<!-- screenshot of this happening. -->

This is how HTTP/1.1 works. One computer (the server) listens on
a well-known port (typically port 80 for outside-facing servers). We
used `nc -l 8000` to listen on port 8000.
Another computer (or even the same computer) connects to this port via
TCP, specifying the IP address and port it wishes to connect to. In our
case, this was the `nc 127.0.0.1 8000` line.

You may now exit either `nc` process by typing
<kbd>Ctrl</kbd> + <kbd>D</kbd> to send an end-of-file. The other `nc`
process should also exit. You may also close one of the two terminals.

Backwards engineering an HTTP request
-------------------------------------

Create another TCP server using netcat, listening on port 8000.
The command to do this is:

    nc -l 8000

With `nc` waiting for a connection, open up your web browser of choice.
Navigate to <http://localhost:8000/hello>. `nc` should be displaying a lot
more text.

> **Question 2**. Copy-paste the output of `nc` as the answer to this
> question.

Type "hello", press <kbd>Enter</kbd>, then press <kbd>Ctrl</kbd> + <kbd>C</kbd>
to close the connection.

> **Question 3**. If you got an error message, copy-paste the error
> message from your browser as the answer to this question. If your
> browser simply says "hello", answer this question with the name of
> your browser.

What just happened is that our browser tried to connect to an HTTP
server called "localhost:8000". The server it connected to is the `nc`
program running in your terminal. The browser sends an HTTP request as
plain, ASCII text, and is waiting for a reply. You typed "hello" and
pressed enter, which confused your browser. "That's not an HTTP
response!" says your browser.


Understanding the HTTP request
------------------------------

In this section, we will form an understanding of the byte-by-byte
details of the HTTP request. Redirect the output of `nc` to a file
called `request.txt`. We can do this by using the following command:

    nc -l 8000 | tee request.txt

In a new tab in your browser, navigate to <http://localhost:8000/hello>.
Type the following into `nc`:

```
HTTP/1.1 204 No Content
Connection: close

```

And press <kbd>Enter</kbd> twice. `nc` should have quit, and your
browser should no longer be attempting to load from your server. The
request that your browser attempted should be in `request.txt`.

Open `request.txt` in a text editor of your choice.

> **Question 4**. How many lines does `request.txt` have? Include any
> empty lines in your count. Where do empty lines (if any) appear in
> this file?

An open problem in computing science is how to specify a newline in a text
file. For ASCII (and its derivatives), here are a few of the ways that
computer systems use to indicate the end of the file.

 - CR: Using a carriage return character (`0d` in hexadecimal)
 - LF: Using a line feed  character (`0a` in hexadecimal)
 - CRLF: Using a carriage return, followed by a line feed character (`0d`, followed by `0a` in hexadecimal)

Use the `xxd` program to output a **hexadecimal dump** of the bytes in
the `request.txt` file.

```
xxd request.txt
```

<aside>
<header>Tips on reading hexadecimal</header>
<p> Each pair of <strong>two</strong> hexadecimal digits is one byte. So
<code>0a</code> is one bytes, whereas <code>0d0a</code> is two bytes.
A single hexadecimal digit represents 4 bits, which is also colloquially
known as a “<a href="https://en.wikipedia.org/wiki/Nibble">nibble</a>”.
</p>
</aside>


> **Question 5** Inspecting `request.txt` using `xxd`, how does HTTP
> specify line endings? Is it CR, LF, or CRLF? Specify the byte offset
> of the **first** line ending in `request.txt` (that is, the index of
> the first time you see either the line ending, which is one of CR, LF,
> or CRLF).

Inspect the HTTP request in `request.txt`. Notice the structure of the
file. The first line is the **request line**:

    METHOD /path/of/resource/ HTTP/1.1

For example, your browser made a `GET` request for the resource with the
path `/hello`, so your answer to Question 2 should start with the
following line:

    GET /hello HTTP/1.1

(We will cover HTTP methods in a future lab).

After the **request line**, is one or more **HTTP headers**. In
HTTP/1.1, one of these headers  **must** be the `Host` header. For
example, your answer from Question 2 should have included the line:

    Host: localhost:8000

> **Question 6**: Using your current knowledge of web protocols, why is
> the `Host` header required in all HTTP/1.1 requests? Try to answer
> this question without consulting external resources (i.e., don't do
> a Google search or consult a textbook).

Most `GET` requests include a few more headers, indicating the type of
entity it's requesting. For example, your browser indicated that it will
_accept_ entities of many types, but it will prefer an HTML web page.

> **Question 7** Copy-paste the value of the `Accept` header as the
> answer to this question.

Finally, the HTTP request is ended by a completely empty line.

> **Question 8** what are the last four bytes (expressed in hexadecimal)
> of the HTTP request contained with `request.txt`? Use `xxd` to get
> a hexadecimal dump of the bytes in `request.txt`.

To summarize, the generic structure of an HTTP request is as follows:

    <status line> <newline>
    <one or more request headers, one per line> <newline>
    <empty line> <newline>

Where headers have the following syntax:

    <header name>: <header value> <newline>

An example HTTP request looks like this:

<pre><code>GET /hello HTTP/1.1
Host: localhost:8000
Accept: text/html, */*;q=0.1

</code></pre>

Let's GET that cat meme!
------------------------

Before we are able to use netcat to fetch that cat meme, we need to know
the IP address of the server hosting it.

The host is called `www.eddieantonio.ca`. Use the `dig` command to get
the IP address of this host.

    dig +short www.eddieantonio.ca

(If there are multiple lines of output, use the line of output in the
form `<number>.<number>.<number>.<number>`).

> **Question 9**: What is the IP address of `www.eddieantonio.ca`?

Use your favorite text editor to create an HTTP request to fetch that cat meme
mentioned earlier. You will create a file called `my-request.txt`.
This file will have the HTTP request: the HTTP status line, two HTTP
headers, and an empty line. Here is all the information that your HTTP
request should have:

 - It should use the `GET` method to make the request
 - It should request the **path** `/cmput296/lab-3/cat-meme.jpg`
 - The **host** is `www.eddieantonio.ca`
 - `cat-meme.jpg` is an image, so the request should specify that it
   will `Accept` an image. The value of the `Accept` header should be
   `image/jpeg,image/*;q=0.1`

Once you are done creating the HTTP request in your text editor, save it
as `my-request.txt`.

> **Question 10**: Copy-and-paste the HTTP request you just created as
> the answer to this question. You may refine the HTTP request until you
> get it right.

Finally, we'll use netcat to send our HTTP request to the server, and
save its response. In the following line, replace `IPADDRESS` with the
IP address of `www.eddieantonio.ca`, and run it.

    cat my-request.txt | nc IPADDRESS 80 | tee response.bin

If it worked, you should see a lot of gibberish scroll on your terminal.
To prove that it worked, open `response.bin` in a text editor. Delete
the HTTP request headers at the top of the file (including the empty
line!), then save the file as `cat-meme.jpg`. You should now be able to
open the file in an image viewer of your choice.
