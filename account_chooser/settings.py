from django.conf import settings
from django.core.urlresolvers import reverse


def _get_settings():
    _default_settings = {
        'loginUrl': getattr(settings, 'LOGIN_URL'),  # Login URL.
        'signupUrl': '/accounts/signup/',  # Signup URL.
        'userStatusUrl': reverse('account_chooser_get_user_status'),  # User status URL.
        'homeUrl': getattr(settings, 'LOGIN_REDIRECT_URL'),  # Home page URL.
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

ACCOUNT_CHOOSER_SETTINGS = _get_settings()
