#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright 2018 Eddie Antonio Santos <easantos@ualberta.ca>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Serves a webpage for writing JavaScript, and a few dynamic endpoints
for testing AJAX.
"""

import json
import http.server
import urllib.parse
import traceback


class InvalidRequest(Exception):

    """
    An exception raised to prevent returning to the normal do_X handler.
    """


class AJAXRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """
        Handle a GET request to:

            /       -- index
            /calc/  -- calculator

        Respond with 404 for anything else.
        """

        # What BaseHTTPRequestHandler calls  "path"
        # is actually the request target. i.e., path + query
        components = urllib.parse.urlparse(self.path)
        path = components.path
        self.query_raw = components.query
        self.query = urllib.parse.parse_qs(self.query_raw)
        if path == '/':
            self.do_GET_index()
        elif path == '/calc/':
            self.do_GET_calc()
        else:
            self.do_404()

    def do_GET_index(self):
        """
        Serve index.html.
        """
        try:
            with open('index.html', 'rb') as index_file:
                body = index_file.read()
        except IOError:
            return self.client_error(
                'You must create a page called index.html '
                'in the current working directory',
                status_code=404
            )
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET_calc(self):
        """
        A simple calculator. Requires query parameters of 'a', 'b', and 'op'.
        'op' is '+', '-', '*', '/'; 'a' and 'b' will be parsed as floats.

        The response will depend on the Accept header.
        """
        a, b, op = self.parse_calc_query_params()
        answer = {
            '+': lambda: a + b,
            '-': lambda: a - b,
            '*': lambda: a * b,
            '/': lambda: a / b,
        }[op]()

        accept_types = self.get_accept_types()
        if 'application/json' in accept_types:
            body = json.dumps({'answer': answer}).encode('UTF-8')
        else:
            # Assume it accepts HTML
            body = '<p> The answer is {0} </p>'.format(answer).encode('UTF-8')

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def parse_calc_query_params(self):
        q = self.query
        if 'a' not in q or 'b' not in q or 'op' not in q:
            self.client_error(
                'Did not get proper query arguments! '
                'I expected ?a=...&b=...&op=... '
                'But I actually got {0}'.format(self.query_raw)
            )
        a, b, op = q['a'][-1], q['b'][-1], q['op'][-1]
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            self.client_error(
                'Invalid value for a ({0!r}) and/or b ({1!r})'.format(a, b)
            )

        if op not in '+-/*':
            self.client_error(
                'Invalid value for op. should be one of '
                "'+', '-', '*', '/' but actually got " + repr(op)
            )
        return a, b, op

    def get_accept_types(self):
        accepts = self.headers.get('Accept', None)
        if accepts:
            return accepts.split(',')
        else:
            return []

    def do_404(self):
        """
        Responds with a simple 404.
        """
        self.send_response(404)
        self.end_headers()

    def client_error(self, err_msg, status_code=400):
        """
        Called when a 400 client error is required.
        """
        body = str(err_msg).encode('UTF-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/plain; charset=UTF-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        raise InvalidRequest

    def server_error(self, err_msg='Server error! See logs'):
        """
        Should be called when there's an unhandled exception.
        """
        traceback.print_exc()
        body = str(err_msg).encode('UTF-8')
        self.send_response(500)
        self.send_header('Content-Type', 'text/plain; charset=UTF-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    host, port = 'localhost', 8000
    server = http.server.HTTPServer((host, port), AJAXRequestHandler)
    print("Listening on http://{0}:{1}/".format(host, port))
    server.serve_forever()
