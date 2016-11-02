% CMPUT 404 Lab 9
% Alexander Wong, Eddie Antonio Santos
% November 2, 2016

# Overview

 - Understand the basics of authentication for web-based applications
 - Understand what HTTP Basic Authentication, HTTP TOken Authentication
   and HTTP Session Authentication are.
 - Understand what OAuth and OAuth2 are.

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
 #. Navigate to the `iguana` application, migrate the Django application.
 #. Within the iguana application, create a superuser.
 #. Run the iguana application on the default settings (localhost:8000)
 #. Run the leopard application on a operate port (e.g., 9000)
 #. Use the leopard application to query the iguana application's user
    API using the three authentication methods

# Questions

**Remember to cite your sources!**

 #. Provide example header(s) for
    HTTP Basic Authentication, HTTP Token Authentication, and HTTP
    Session  Authentication.
 #. What is OAuth and OAuth2? Who uses it?
 #. What authentication did you use to login to eClass?
 #. Which type of authentication would you use for an unencrypted
    connection?
