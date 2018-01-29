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

In this section, we will form an understanding of the byte-by-byte details of the HTTP
request.

Download
<a href="./lab-3/response.bin" download><code>response.bin</code></a>
and save it to the same directory as where you're running `nc`.

Now, redirect `nc`'s input to come from `response.bin`, and write `nc`'s
output to a file called `request.txt`. We can do both of these by using
the following command:

```sh
cat response.bin | nc -l 8000 | tee request.txt
```

Once again, go to your browser and navigate to
<http://localhost:8000/hello>.

> **Question 4**. What happened in your browser when you navigated to
> <http://localhost:8000/hello>? Copy-paste any text that appeared in
> your browser here.

Open `request.txt` in your text editor of choice.

> **Question 5**. How many lines does `request.txt` have? Include any
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
xxd requests.txt
```

> **Question 6** Inspecting `request.txt` using `xxd`, how does HTTP
> specify line endings? Is it CR, LF, or CRLF? Specify the byte offset
> of the **first** line ending in `request.txt` (that is, the index of
> the first time you see either the line ending, which is one of CR, LF,
> or CRLF).
