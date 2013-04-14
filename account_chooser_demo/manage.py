#!/usr/bin/env python
import os
import sys

# hack to allow importing account_chooser
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     os.path.pardir)))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "account_chooser_demo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

