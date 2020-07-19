Deployment
----------

This section contains a step-by-step guidance how to deploy this software.
It`s based on a deployment of Django with Apache2 and mod_wsgi on a raspberry pi 4.

Sources:
~~~~~~~~

* https://docs.djangoproject.com/en/3.0/howto/deployment/
* https://wiki.ubuntuusers.de/Apache_2.4/
* https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04

Requirements:
~~~~~~~~~~~~~

* a web server
* basic knowledge of bash

Basic configuration:
~~~~~~~~~~~~~~~~~~~~

Update your distro

  ``sudo apt update && sudo apt upgrade``

Install Dependencies for the deployment. (We use Python3)

  ``sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3``

You also need to install virtualenv, to seperate Python from your system's python

  ``sudo pip install virtualenv``

Now we need to clone the Git-Repository and setup the virtualenv for Python.
First you need to change to the directory that you want to clone this web application to.
Then:

  ``git clone https://github.com/mribrgr/StuRa-Mitgliederdatenbank.git``
  ``cd StuRa-Mitgliederdatenbank/``

Now create a virtual environment and activate it.

  ``virtualenv venv``
  ``source venv/bin/activate``

If you have successfully activated your virtual ennvironment than your prompt should
look something like this ``(venv) user@host:StuRa-Mitgliederdatenbank``. The last
step is to install the requirements.txt in the virtual environement.

  ``pip install -r requirements.txt``

Adjust Django Project Settings:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First we need to configure ``StuRa-Mitgliederdatenbank/bin/settings.py``:
We open the file first (based on the previous chapter)

  ``nano bin/settings.py``

Here we need to register our server's public IP address or domain name.

  ``ALLOWED_HOSTS = ["IP_or_DOMAIN"]``

At the bottom of the settings.py we need to define a static directory for our static html files.

  ``STATIC_ROOT = os.path.join(BASE_DIR, 'mystatic/')``

Now we can close and save the file.
The last step is to do initial commands:

  | ``python ./manage.py makemigrations``
  | ``python ./manage.py migrate``
  | ``python ./manage.py collectstatic``
  | ``python ./manage.py createsuperuser``

And deactivate the virtual environment

  ``deactivate``

Configure Apache2:
~~~~~~~~~~~~~~~~~~

To enable Apache2 as front end we need to configure WSGI pass.
To achieve this we need to edit the default virtual host file:

  ``sudo nano /etc/apache2/sites-available/000-default.conf``

We can keep everything that is present in this file and add our config above
the last ``</VirtualHost>`` tag. What we first specify is the static directory
and the path to the wsgi.py.
(In this Example I have cloned the directory in ~/StuRa-Mitgliederdatenbank)
(pi is my username change it to yours)

.. code-block:: bash
  :caption: /etc/apache2/sites-available/000-default.conf

  <VirtualHost *:80>

    . . .

    Alias /static /home/pi/StuRa-Mitgliederdatenbank/mystatic
    <Directory /home/pi/StuRa-Mitgliederdatenbank/mystatic>
        Require all granted
    </Directory>

    <Directory /home/pi/StuRa-Mitgliederdatenbank/bin>
      <Files wsgi.py>
        Require all granted
      </Files>
    </Directory>

  </VirtualHost>

Now we add the recommended deamon mode to the WSGI process.

.. code-block:: bash
  :caption: /etc/apache2/sites-available/000-default.conf

  <VirtualHost *:80>

    . . .

    Alias /static /home/pi/StuRa-Mitgliederdatenbank/mystatic
    <Directory /home/pi/StuRa-Mitgliederdatenbank/mystatic>
        Require all granted
    </Directory>

    <Directory /home/pi/StuRa-Mitgliederdatenbank/bin>
      <Files wsgi.py>
        Require all granted
      </Files>
    </Directory>

    WSGIDaemonProcess StuRa-Mitgliederdatenbank python-home=/home/pi/StuRa-Mitgliederdatenbank/venv python-path=/home/pi/StuRa-Mitgliederdatenbank
    WSGIProcessGroup StuRa-Mitgliederdatenbank
    WSGIScriptAlias / /home/pi/StuRa-Mitgliederdatenbank/bin/wsgi.py

  </VirtualHost>

Solve some Permission Issues:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step is to change the permissions of the database, so that group owner
can read and write. Then we need to the ownership of some files to Apache2
group and user ``www-data``.

  | ``chmod 664 ~/StuRa-Mitgliederdatenbank/db.sqlite3``
  | ``sudo chown www-data:www-data ~/myproject/db.sqlite3``
  | ``sudo chown www-data:www-data ~/myproject``

If you got firewall issues, allow Apache to acces the firewall example:

  ``sudo ufw allow 'Apache Full'``

Last but not least check the Apache files if everything is correct:

  ``sudo apache2ctl configtest``

If the output looks like ``Syntax OK`` you are done and can restart your apache2
service:

  ``sudo systemctl restart apache2``
