#!/usr/bin/env python
from django.core.management import execute_manager
import imp, os, sys


try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.join(path, '..'))

if __name__ == "__main__":
    execute_manager(settings)
