% Lab 3: HTTP from scratch
% CMPUT 296; written by Eddie Antonio Santos
% January 29, 2018

Overview
========

 - Learn how to create a TCP connection on the command line
 - Use the TCP connection backwards engineer an HTTP request
 - Create our own HTTP requests

Materials
=========

 - An internet connection
 - A modern web browser (like Firefox or  Google Chrome)
 - Unix command line tools: `dig`, `nc` (netcat), `xxd`


Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**. Questions look like this.

**Remember to cite your sources**.

In last weeks labs, we spied on how your browser creates HTTP requests
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

Other CMPUT courses will cover how the network layers up to TCP/IP work,
however, in this course, we can use the `netcat` program to establish
fresh TCP connections; either to as a client to a server, or setup
a server ourselves.

We will create a process to **listen** to TCP connections. This will be
our server. To do this, do the following in the command line:

```sh
nc -l 8000
```

You have established a new TCP server, listening on **port 8000** for new
connections.

To test this, open a new terminal, and connect to your server by
invoking:

```sh
nc 127.0.0.1 8000
```

This command means, connect to the computer with IP address `127.0.0.1`,
and connect to port 8000 (as a client).

> **Question 1**. What computer does 127.0.0.1 refer to?

Now, with both terminals running `nc` on your screen, type something
into one of the terminals. If all went well, you should be seeing the
text appear in the other terminal. Congratulations! You just used TCP to
send a message from one process to another process!

> screenshot of this happening.

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

```sh
nc -l 8000
```

With `nc` waiting for a connection, open up your web browser of choice.
Navigate to <http://localhost:8000/hello>. `nc` should be displaying a lot
more text.

> **Question 2**. Copy-paste the output of `nc` as the answer to this
> question.

Type "hello", press <kbd>Enter</kbd>, then press <kbd>Ctrl</kbd> + <kbd>C</kbd>
to close the connection.


> **Question 3**. Copy-paste the error message from your browser as the
> answer to this question.

What just happened is that our browser tried to connect to an HTTP
server called "localhost:8000". The server it connected to is the `nc`
program running in your terminal. The browser sends an HTTP request as
plain, ASCII text, and is waiting for a reply. You typed "hello" and
pressed enter, which confused your browser. "That's not an HTTP
response!" says your browser.

Understanding the HTTP request
------------------------------

Let's form an understanding of the byte-by-byte details of the HTTP
request. We're going to create an appropriate HTTP response.




<!--

Create requests in a text editor of your choice.

-->

<!--

Attach Accept-Encoding to server

Get the uncompressed data.

Report the file size.

gunzip the content

Report the file size again.

https://github.com/jvns/gzip.jl

-->

<!--

Omit the Host header to example.com

-->

<!-- manually fetch IP addresses with dig -->

<!--

Make them construct an HTTP request

-->
