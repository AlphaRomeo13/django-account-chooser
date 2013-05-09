from copy import deepcopy
from django.conf import settings
from django.test import TestCase
from account_chooser.settings import _get_settings
from django.core.urlresolvers import reverse


class GetAccountChooserSettingsTest(TestCase):
    _overriden_settings = {
        'signupUrl': '/accounts/register/',
        'siteEmailId': 'id_email',
        'sitePasswordId': 'id_password',
        'siteDisplayNameId': 'id_username',
        'sitePhotoUrlId': '',
        'providers': {
                      "facebook.com": '/facebook/connect',
                      "twitter.com": '/twitter_auth',
                      "google.com.com": '/gplus_auth',
        },
    }
    _default_settings = {
        'loginUrl': getattr(settings, 'LOGIN_URL'),
        'signupUrl': '/accounts/signup/',
        'userStatusUrl': reverse('account_chooser_get_user_status'),
        'homeUrl': getattr(settings, 'LOGIN_REDIRECT_URL'),
        'siteEmailId': 'email',
        'sitePasswordId': 'password',
        'siteDisplayNameId': '',
        'sitePhotoUrlId': '',
        'uiConfig': '',
        'language': 'en',
        'providers': [],
    }

    def test_update_default_settings(self):
        delattr(settings, 'ACCOUNT_CHOOSER_SETTINGS')
        ac_settings, ac_providers = _get_settings()
        self.assertDictEqual(ac_settings, self._default_settings)
        self.assertDictEqual(ac_providers, {})

        with self.settings(ACCOUNT_CHOOSER_SETTINGS=self._overriden_settings):

            desired_providers = deepcopy(self._overriden_settings['providers'])
            desired_settings = deepcopy(self._overriden_settings)
            desired_settings.update({
                'loginUrl': getattr(settings, 'LOGIN_URL'),
                'userStatusUrl': reverse('account_chooser_get_user_status'),
                'homeUrl': getattr(settings, 'LOGIN_REDIRECT_URL'),
                'language': 'en',
                'uiConfig': '',
                'providers': ['facebook.com', 'twitter.com', 'google.com.com'],
            })
            ac_settings, ac_providers = _get_settings()
            self.assertDictEqual(ac_settings, desired_settings)
            self.assertDictEqual(ac_providers, desired_providers)
