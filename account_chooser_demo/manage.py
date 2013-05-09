#!/usr/bin/env python
from django.core.management import execute_manager
import imp

# hack to allow importing account_chooser
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
#                                     os.path.pardir)))

try:
    imp.find_module('account_chooser_demo/settings')
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find file 'settings.py' in the directory"
                     " containing %r. It appears you've customized things."
                     "\nYou'll have to run django-admin.py, passing it your"
                     " settings module.\n" % __file__)
    sys.exit(1)

import account_chooser_demo.settings as settings
settings.ROOT_URLCONF = 'account_chooser_demo.urls'

if __name__ == "__main__":
    execute_manager(settings)
