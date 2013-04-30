import os

from django.test import TestCase
from django.template.loader import get_template
from django.template.context import Context
from django.core.management import call_command

from account_chooser.settings import ACCOUNT_CHOOSER_SETTINGS


class ManagementCommandTest(TestCase):
    def test_configureac_command(self):
        call_command('configureac')
        _context = Context(ACCOUNT_CHOOSER_SETTINGS)
        template = get_template('account_chooser/djac-conf.txt')
        prepared_data = template.render(_context)
        path_to_app = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   '/'.join([os.path.pardir, os.path.pardir])))
        js_file = open(path_to_app +
                       '/account_chooser/static/js/djac-config.js', 'r').read()
        self.assertEqual(prepared_data, js_file)