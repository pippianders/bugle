# bugle

Group collaboration tools for hackers in forts.

Dependencies:

- Several collaborating hackers
- A fort, castle or other defensive structure
- No internet connection

Bugle is a Twitter-like application for groups of hackers collaborating in a 
castle (or fort, or other defensive structure) with no internet connection.
Bugle combines Twitter-style status updates with a pastebin and a group todo
list. It also has a rudimentary API allowing automated scripts (such as the 
included subversion post-commit hook) to post messages in an unobtrusive way.

It was built as a side project during a [/dev/fort](http://devfort.com/) week 
in a Scottish castle. See [AUTHORS](AUTHORS.txt) for contributors.

Bugle is released under a BSD license.

## Important note

Bugle isn't secure (vulnerable to CSRF) and doesn't scale.

# Development installation

Fabric is required (or do the `setup_dev` stuff yourself):
    
    $ pip install fabric

To set up a development environment:

    $ sudo -u postgres createdb -O `whoami` bugle
    $ fab localhost setup_dev 
    $ cd bugle_project/
    $ ./manage.py syncdb
    $ ./manage.py migrate

If ``requirements.txt`` gets updated in the future, you may need to run:

    $ fab localhost install_requirements

# Setting up live server

Before deploying for the first time, install Apache and mod-wsgi 
(``libapache2-mod-wsgi`` on Debian).

Create database ``bugle`` and an SSL certificate:

    $ sudo -u postgres createuser -P -D -S -R bugle
    [enter password for bugle user]
    $ sudo -u postgres createdb -O bugle bugle
    $ make-ssl-cert generate-default-snakeoil --force-overwrite
    $ a2enmod ssl

Set up the deployment environment:

    $ fab live setup

## Deployment

To deploy new versions:

    $ fab live create_version deploy
