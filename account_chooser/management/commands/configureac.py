"""
build the javascript file that configures account chooser for you
make sure you added the ACCOUNT_CHOOSER_SETTINGS in your settings file
"""
import os

from account_chooser.settings import ACCOUNT_CHOOSER_SETTINGS
from django.core.management.base import NoArgsCommand
from django.template.loader import get_template
from django.template.context import Context


class Command(NoArgsCommand):
    help = "build the javascript file that configures account chooser for you"
    "make sure you added the ACCOUNT_CHOOSER_SETTINGS in your settings file"

    def handle_noargs(self, **options):
        path_to_app = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                '/'.join([os.path.pardir, os.path.pardir])))
        _context = Context(ACCOUNT_CHOOSER_SETTINGS)
        template = get_template('account_chooser/djac-conf.txt')
        js_file = open(path_to_app + '/static/js/djac-config.js', 'w+')
        js_file.write(template.render(_context))

