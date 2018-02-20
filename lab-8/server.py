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

import http.server
import traceback


class AJAXRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.do_GET_index()
        elif self.path == '/calc/':
            self.do_GET_AJAX()
        else:
            self.do_404()

    def do_POST(self):
        ...

    def do_GET_index(self):
        try:
            with open('index.html', 'rb') as index_file:
                body = index_file.read()
        except Exception:
            self.server_error()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

    def do_404(self):
        self.send_response(404)
        self.end_headers()

    def server_error(self, err_msg='Server error! See logs'):
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
