% CMPUT 404 Lab 9
% Alexander Wong, Eddie Antonio Santos
% November 2, 2016

# Overview

 - Understand the basics of authentication for web-based applications.
 - Understand what HTTP Basic, HTTP Token, and HTTP Session
   Authentication are.
 - Understand what OAuth and OAuth2 are.
 - Understand the security implications of authentication schemes.

[repo]: https://github.com/CMPUT404W2016/CMPUT404LAB9_W2016

# Steps

 #. Clone [this repository][repo]
 #. Create a Python virtual environment and install the requirements.

    ```sh
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

 #. Navigate to the `leopard` application, migrate the Django application.

    ```sh
    cd leopard
    python manage.py migrate
    ```

 #. Navigate to the `iguana` application, migrate the Django application.

    ```sh
    cd ../iguana
    python manage.py migrate
    ```

 #. Within the `iguana` application, create a superuser.

    ```sh
    python manage.py createsuperuser
    ```

 #. Run the `iguana` application on port 8000.

    ```sh
    python manage.py runserver 8000
    ```

 #. Open a new terminal, activate the virutalenv and run the `leopard`
    application on a port 9000.

    ```sh
    source venv/bin/activate
    cd leopard
    python manage.py runserver 9000
    ```

 #. Use the `leopard` application to query the `iguana` application's
    user API using the three authentication methods: no authentication,
    HTTP Basic, and HTTP Token. Use the username and password for the
    superuser you created for the `iguana` application.

# Hints

Examine the source of the `leopard` app! Particularly `consumer/views.py`.

# Questions

**Remember to cite your sources!**

 #. Provide an example HTTP **request** header(s) for authentication
    with HTTP Basic Authentication. Use username `cmput404` and password
    `skruntskrunt`.
 #. Briefly explain the actors (end-user, user-agent(s), server(s)),
    involved in HTTP Token Authentication, and a sequence of how an
    end-user will authenticate (like a UML sequence diagram, but
    you do not need to draw or submit a diagram).
 #. Provide example HTTP **response** header(s) for authentication with HTTP
    Session Authentication.
 #. What is OAuth and OAuth2? Name one OAuth2 provider.
 #. Assume a client and a server are using HTTP over an unencrypted
    connection. Explain how you would hijack the client's authentication
    if they are using HTTP basic authentication, HTTP token
    authentication, and HTTP session authentication.
 #. What type of authentication did you use to login to eClass?
