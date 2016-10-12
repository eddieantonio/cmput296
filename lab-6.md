% CMPUT 404 Lab 6
% Alexander Wong, Eddie Antonio Santos
% October 12, 2016

## Overview

Learn how to host a Django application on a PaaS (OpenShift).
Learn about the other cloud application PaaS services available (AWS,
Windows Azure, Google App Engine).

## OpenShift Steps

Steps are derived from the `openshift-django` repository: <https://github.com/awwong1/openshift-django>

 #. Sign up for a free account at <https://openshift.com>
 #. Click "Create your first application now", and find the Python 2.7 cartridge.
 #. Set your namespace and application name, click "Create Application"
    (This may take 5-10 minutes)
 #. Install the OpenShift CLI tools

    If you're on a lab machine:

    ```bash
    gem install --user-install net-ssh -v 2.9.2
    gem install --user-install rhc
    # Note: enter the following two commands EXACTLY one after the
    # other (fc -ln -1 copies the last command to your startup file)
    export PATH=$PATH:$HOME/.gem/ruby/1.9.1/bin
    fc -ln -1 >> ~/.bashrc
    ```

    Else if you're on your own personal machine:

    ```bash
    sudo gem install rhc
    ```

 #. Log into your OpenShift account from the terminal

    ```bash
    rhc setup
    ```

 #. Clone your application locally to your workspace

    List your apps; find the name of the app you want to clone.

    ```bash
    rhc apps
    ```

    Clone that app (replace `{app-name}` with your app's name):


    ```bash
    rhc git-clone {app-name}
    cd {app-name}
    ```

 #. Add a database cartridge to your application.

    Chose either PostgreSQL:

    ```bash
    rhc add-cartridge postgresql-9.2
    ```

    Or MySQL:

    ```bash
    rhc add-cartridge mysql-5.5
    ```

 #. Add the Django seed repository as the upstream repository:

    ```bash
    git remote add upstream -m master https://github.com/awwong1/openshift-django.git
    git pull -s recursive -X theirs --allow-unrelated-histories upstream master
    ```

 #. Set the WSGI application to be Django's built-in WSGI application

    ```bash
    rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=wsgi.py --app {app-name}
    ```

 #. Push the repo to OpenShift:

    ```bash
    git push
    ```

 #. SSH into the application to create a Django superuser.

    ```bash
    rhc ssh
    python app-root/repo/manage.py createsuperuser
    ```

 #. Now use your browser to connect to the admin site. The URL will be
     of the form:

     ```
     https://{app-name}-{your-openshift-username}.rhcloud.com/admin/
     ```

     You should be able to login to Django's admin panel!


## Questions

 1. What does WSGI stand for? What does it do?
 2. What does PaaS stand for?
 3. What are some of the benefits to using a PaaS to host your
    applications?
    What are some of the drawbacks?
 4. List three different PaaS vendors. Also specify the vendor you are
    (likely) going to use for your CMPUT 404 project.
 6. How many Git remotes does your repository have? Explain how each
    entry got there and why it's there (hint: use `git remote -v`).
 5. What is your OpenShift application URL (for this lab's code)?
