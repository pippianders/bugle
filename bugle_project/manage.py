#!/usr/bin/env python

from __future__ import print_function

import os
import sys
from functools import partial

# We want a few paths on the python path; where are we? eh?
project_path = os.path.realpath(os.path.dirname(__file__))
# Next add the root above the project so we can have absolute paths everywhere
repo_path = os.path.join(project_path, '../')

# we add them first to avoid any collisions
sys.path.insert(0, project_path)
sys.path.insert(0, repo_path)

from django.core.management import execute_manager

args = sys.argv
# Let's figure out our environment
if os.environ.has_key('DJANGOENV'):
    environment = os.environ['DJANGOENV']
elif len(sys.argv) > 1:
    # this doesn't currently work
    environment = sys.argv[1]
    if os.path.isdir(os.path.join(project_path, 'settings', environment)):
        sys.argv = [sys.argv[0]] + sys.argv[2:]
    else:
        environment = None
else:
    environment = None

try:
    module = "configs.%s.settings" % environment
    __import__(module)
    settings = sys.modules[module]
    # worked, so add it into the path so we can import other things out of it
    sys.path.insert(0, os.path.join(project_path, 'configs', environment))
except ImportError:
    environment = None

# We haven't found anything helpful yet, so use development.
if environment is None:
    print_stderr = partial(print, file=sys.stderr)
    
    try:
        print_stderr("No environment found: using development")
        import configs.development.settings
        settings = configs.development.settings
        environment = 'development'
        sys.path.insert(0, os.path.join(project_path, 'configs', environment))
    except ImportError:
        print_stderr("Error: Can't find the file 'settings.py'; "
                     "looked in %s and common." % (environment,))
        print_stderr("(If the file settings.py does indeed exist, it's "
                     "causing an ImportError somehow.)")
        sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
