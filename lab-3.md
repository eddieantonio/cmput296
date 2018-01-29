% Lab 3: HTTP from scratch
% CMPUT 296; written by Eddie Antonio Santos
% January 29, 2018

Overview
========

Materials
=========

 - An internet connection
 - Unix-like command line tools: `dig`, `nc` (netcat), `xxd`

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

In order for your computer to be able to retrieve this cat meme from
internet, it must do a few things at several layers of abstraction:

 1. Physical layer: it must transfer bits of information through some
    physical mediums, such as modulating the voltage on a wire, or
    modulating a carrier radio wave.
    Our request for a cat meme will be converted into bits on a wire. 
 2. Link layer: it must have a way of organizing and directing
    those bits to a specific device (such as a router) on the local
    network. The unit of organization is called a _packet_.
    The bytes for our request for a cat image will be grouped into one
    or more data packets which are destined to our router.
 3. Internet layer: in order for those packets to be directed to
    a device on a _different_ network, there must be a way to address
    any computer in the world. This is the IP layer, and where IP
    addresses come in to play.
    Our request for a cat meme is destined for the machine at 
    `151.101.149.147`, which happens to be running an HTTP server,
    hosting the cat meme we want. An IP packet specifies that our
    request is destined for this machine.
 4. Transport layer: for some applications, we need to ensure that our
    packets are properly received, and that there are ways to deal with
    any errors along the way. This way we can establish a _reliable
    transport mechanism_ that allows us to send bytes knowing that the
    other end will get them, no matter how many networks that packet has
    to hop through. For this, there is TCP.
    Our request for a cat meme happens after our computer and the
    external server make a "handshake" to establish that they will be
    talking to each other. We send the bytes of our request in one or
    more TCP packets, to which the server must reply and say "got it"
    for each one.
 5. Application layer: HTTP. 

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
