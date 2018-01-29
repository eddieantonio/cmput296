% Lab 4: Advanced HTTP
% CMPUT 296; written by Eddie Antonio Santos
% January 29, 2018

Overview
========

Materials
=========

 - An internet connection
 - Unix-like command line tools: `dig`, `nc` (netcat), `gunzip`

Procedure
=========

Submit your responses to the questions in this lab on eClass.

> **Question X**. Questions look like this.

**Remember to cite your sources**.

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


Now, the bytes that your browser sent should be stored in the file
called `request.txt`. Use the `xxd` program to retrieve a hexadecimal
dump of the file's bytes:


```sh
xxd request.txt
```

> **Question 5**. Copy-paste the hex dump retrieved by typing `xxd
> request.txt` in the terminal as the answer to this question.

The hex dump shows three columns, the first is a hexadecimal offset in
the file; the second are the bytes, expressed in hexadecimal, and last
is an ASCII rendering of the bytes, with bytes that cannot be printed as
ASCII replaced by a period (`.`).

<!--

Download
<a href="./lab-3/response.bin" download><code>response.bin</code></a>
and save it to the same directory as where you're running `nc`.

Now, redirect `nc`'s input to come from `response.bin`, and write `nc`'s
output to a file called `request.txt`. We can do both of these by using
the following command:

```sh
cat response.bin | nc -l 8000 | tee request.txt
```

> **Question ?**. What happened in your browser when you navigated to
> <http://localhost:8000/hello>? Copy-paste any text that appeared in
> your browser here.

-->
