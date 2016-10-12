% CMPUT 404 Lab 6
% Alexander Wong, Eddie Antonio Santos
% October 12, 2016

## Overview

Learn how to host a Django application on a PaaS (OpenShift).
Learn about the other cloud application PaaS services available (AWS,
Windows Azure, Google App Engine).

## OpenShift Steps

 1. Steps are at the openshift-django repository: <https://github.com/awwong1/openshift-django>
 2. Sign up for a free account at <https://openshift.com>
 3. Click "create your first application", select Python 2.7
 4. Set your namespace and application name, click "Create Application"
    (This may take 5-10 minutes)
 5. Install the OpenShift CLI tools

    If you're on a lab machine:

    ```bash
    gem install --user-install net-ssh -v 2.9.2
    gem install --user-install rhc
    # Note: enter the following two commands EXACTLY one after the
    # other (fc -ln -1 copies the last command to your startup file)
    export PATH=$PATH:$HOME/.gem/ruby/1.9.1/bin
    fc -ln -1 >> ~/.bash.rc
    ```

    Else if you're on your own personal machine:

    ```bash
    sudo gem install rhc
    ```

 6. Log into your OpenShift account from the terminal

    ```bash
    rhc setup
    ```

 7. Clone your application locally to your workspace

    List your apps; find the name of the app you want to clone.

    ```bash
    rhc apps
    ```

    Clone that app (replace `{app-name}` with your app's name):


    ```bash
    rhc git-clone {app-name}
    cd {app-name}
    ```

 8. Add a database cartridge to your application.

    Chose either PostgreSQL:

    ```bash
    rhc add-cartridge postgresql-9.2
    ```

    Or MySQL:

    ```bash
    rhc add-cartridge mysql-5.5
    ```

 9. Add the Django seed repository as the upstream repository:

    ```bash
    git remote add upstream -m master https://github.com/awwong1/openshift-django.git
    git pull -s recursive -X theirs --allow-unrelated-histories upstream master
    ```

 10. Set the WSGI application to be Django's built-in WSGI application

    ```bash
    rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=wsgi.py --app {app-name}
    ```

 11. Push the repo to OpenShift:

    ```bash
    git push
    ```

 12. SSH into the application to create a Django superuser.

    ```bash
    rhc ssh
    python app-root/repo/manage.py createsuperuser
    ```

 13. Now use your browser to connect to the admin site.


## Questions

 1. What does WSGI stand for? What does it do?
 2. What does PaaS stand for?
 3. What are some of the benefits to using a PaaS to host your
    applications?
    What are some of the drawbacks?
 4. List three different PaaS vendors. Also specify the vendor you are
    (liekly) going to use for your CMPUT 404 project.
 6. How many Git remotes does your repository have? Explain how each
    entry got there and why it's there (hint: use `git remote -v`).
 5. What is your OpenShift application URL (for this lab's code)?
