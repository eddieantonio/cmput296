% CMPUT 404 Lab 7
% Alexander Wong, Eddie Antonio Santos
% October 19, 2016

# Overview

 - Learn how to create a RESTful web application back-end using [Flask].
 - Set up Heroku with a basic Django application.
 - Research issues concerning client-side scripting.

[Flask]: http://flask.pocoo.org/

# Steps

## Flask

 #. Navigate to a new folder and initialize a new Python virtual
    environment.

    ```bash
    mkdir lab7
    cd lab7
    virtualenv venv
    source venv/bin/activate
    ```

 #. Install Flask.

    ```bash
    pip install Flask
    ```

 #. Create a new Python file named `hello.py` and edit its contents so
    it looks like this:

    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, World!"

    if __name__ == "__main__":
        app.run(debug=True)
    ```

 #. Run the application and navigate to the page in your browser.

    ```bash
    python hello.py
    ```

 #. Navigate back to your terminal and quite the running Flask
 application. Install the Python package `flask-restful`

    ```bash
    pip install flask-restful
    ```

 #. Open up `hello.py` and modify the file so it looks like the
    following:

    ```python
    from flask import Flask
    from flask_restful import Resource, Api

    app = Flask(__name__)
    api = Api(app)

    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

    api.add_resource(HelloWorld, "/")


    if __name__ == "__main__":
        app.run(debug=True)
    ```

 #. Try it in your browser or using cURL.

    ```bash
    curl localhost:5000 # the port may be different on your machine
    ```

 #. Let's implement a fully RESTful application for TODOs. Open up
    `hello.py` and add the following:

    ```python
    from flask import Flask
    from flask_restful import reqparse, abort, Api, Resource

    app = Flask(__name__)
    api = Api(app)

    parser = reqparse.RequestParser()
    parser.add_argument('task')

    # The latest NoSQL key-value store trending on Hacker News.
    TODOs = {
        1: {'task': 'build an API'},
        2: {'task': '????'},
        3: {'task': 'profit'},
    }

    def abort_if_todo_not_found(todo_id):
        if todo_id not in TODOs:
            abort(404, message="TODO {} does not exist".format(todo_id))

    def add_todo(todo_id):
        args = parser.parse_args()
        todo = {'task': args['task']}
        TODOs[todo_id] = todo
        return todo

    class Todo(Resource):
        """
        Shows a single TODO item and lets you delete a TODO item.
        """

        def get(self, todo_id):
            abort_if_todo_not_found(todo_id)
            return TODOs[todo_id]

        def delete(self, todo_id):
            abort_if_todo_not_found(todo_id)
            del TODOs[todo_id]
            return '', 204

        def put(self, todo_id):
            return add_todo(todo_id), 201

    class TodoList(Resource):
        """
        Shows a list of all TODOs and lets you POST to add new tasks.
        """

        def get(self):
            return TODOs

        def post(self):
            todo_id = max(TODOs.keys()) + 1
            return add_todo(todo_id), 201

    api.add_resource(Todo, '/todos/<int:todo_id>')
    api.add_resource(TodoList, '/todos')

    if __name__ == '__main__':
        app.run(debug=True)
    ```

 #. What does the browser show you when you navigate to these pages? Try
    out the following cURL commands:

    ```bash
    curl localhost:5000/todos
    curl localhost:5000/todos/3
    curl -v -X DELETE localhost:5000/todos/2
    curl -v -X POST localhost:5000/todos -d "task=something new"
    curl -v -X PUT localhost:5000/todos/3 -d "task=something different"
    ```

## Heroku

Please follow this guide to set up Django on Heroku:

<https://devcenter.heroku.com/articles/getting-started-with-python#introduction>


# Protip:

[HTTPie] is like cURL, but designed specifically for interacting with
RESTful JSON APIs. It colours output and pretty prints JSON
automatically.

```bash
pip install httpie
http localhost:5000
http :5000
http HEAD :5000
http POST :5000 foo=bar
```

[HTTPie]: https://httpie.org


# Questions

 #. What does REST stand for? What does it mean?
 #. What does CRUD stand for? For each letter in CRUD, give the
    associated HTTP method.
 #. In general, what do HTTP 1xx status codes mean? HTTP 2xx? HTTP 3xx?
    HTTP 4xx? HTTP 5xx?
 #. What is an XSS attack? Name one way a site can be vulnerable to an
    XSS attack.
 #. What does CORS stand for? Under what situation in web application
    development will you need to care about implementing CORS? (Hint:
    What does the "CO" part of "CORS" mean?)
