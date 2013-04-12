"""
A management command which deletes expired accounts (e.g.,
accounts which signed up but never activated) from the database.

Calls ``RegistrationProfile.objects.delete_expired_users()``, which
contains the actual logic for determining which accounts are deleted.

"""

from django.core.management.base import NoArgsCommand
from django.conf import settings
from django.core.urlresolvers import reverse
import os
from django.template.loader import render_to_string, get_template
from django.template.context import Context


class Command(NoArgsCommand):
    help = "Delete expired user registrations from the database"

    def _get_settings(self):
        _default_settings = {
            'loginUrl': getattr(settings, 'LOGIN_URL'),  # Login URL.
            'signupUrl': '/accounts/signup/',  # Signup URL.
            'userStatusUrl': reverse('account_chooser_get_user_status'),  # User status URL.
            'homeUrl': '/',  # Home page URL.
            'siteEmailId': 'email',  # Email input field ID (HTML "id=" attribute value) in the signup and login forms.
            'sitePasswordId': 'password',  # Password input field ID in the signup and login forms
            'siteDisplayNameId': '',  # Display name input field ID in the signup form. Can be set to null or empty if your signup form does not need the user's name.
            'sitePhotoUrlId': '',  # Profile photo URL input field ID in the signup form. Can be set to null or empty if your signup form does not need the user's profile picture.
            'uiConfig': '',  # Values to use in customizing the appearance of the AccountChooser page
            'language': 'en',  # The display language of the AccountChooser page
            'providers': [],  # List of supported Identity Providers, usually given by top-level domain name, for example "facebook.com".
                            }
        _settings = getattr(settings,
                            'ACCOUNT_CHOOSER_SETTINGS', _default_settings)

        for key in _default_settings.keys():
            if key not in _settings:
                _settings.update({key: _default_settings[key]})

        return _settings

    def handle_noargs(self, **options):
        path_to_app = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                '/'.join([os.path.pardir, os.path.pardir])))
        _context = Context(self._get_settings())
        template = get_template('account_chooser/djac-conf.txt')
        js_file = open(path_to_app + '/static/js/djac-config.js', 'w')
        js_file.write(template.render(_context))
