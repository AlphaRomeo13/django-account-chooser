django-account-chooser
======================
[![Build Status](https://travis-ci.org/myaser/django-account-chooser.png)](https://travis-ci.org/myaser/django-account-chooser)
[![Coverage Status](https://coveralls.io/repos/myaser/django-account-chooser/badge.png?branch=master)](https://coveralls.io/r/myaser/django-account-chooser)


it is the django implementation of [account chooser](https://coveralls.io/r/myaser/django-account-chooser)


Quick start
-----------

1. Add "account_chooser" to your INSTALLED_APPS settings::

```python
      INSTALLED_APPS = (
          ...
          'account_chooser',
      )
```
2. Include the account_chooser URLconf in your project urls.py::

```python
      url(r'^accounts/', include('account_chooser.urls')),
```
3. add account-chooser middleware::

```python
      MIDDLEWARE_CLASSES = (
            ...
            'account_chooser.middleware.AccountChooserMiddleware',
        )
```
4. Configure account-chooser in the settings::

    There are a few configuration options to ``account_chooser`` that
    can be placed in a dictionary called ``ACCOUNT_CHOOSER_SETTINGS``:
   * ``loginUrl``

     default is ``getattr(settings, 'LOGIN_URL')``
   * ``signupUrl``

     default is ``'/accounts/signup/'``
   * ``homeUrl``

     where to redirect after ``account_chooser`` signin.
     default is ``getattr(settings, 'LOGIN_REDIRECT_URL')``
   * ``siteEmailId``

     Email input field ID ``(HTML "id=" attribute value)`` in the signup and login forms.
     default is ``'email'``
   * ``sitePasswordId``

     Password input field ID in the signup and login forms.
     default is ``'password'``
   * ``siteDisplayNameId``

     Display name input field ID in the signup form. Can be set to empty if your signup form does not need the user's name.
     default is ``''``
   * ``sitePhotoUrlId``

     Profile photo URL input field ID in the signup form. Can be set to null or empty if your signup form does not need the user's profile picture.
default is ``''``
   * ``uiConfig``

     Values to use in customizing the appearance of the AccountChooser page. consult [user interface customization](http://accountchooser.net/developers/api) for more details.
     default is ``''``
   * ``language``

     The display language of the AccountChooser page.
     default is ``''``
   * ``providers``

     Dict of supported Identity Providers and their login URLs.
     default is ``{}``

   Example configuration::

     ```python
      ACCOUNT_CHOOSER_SETTINGS = {
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
     ```

5. Run the management command configureac to create the javascript file that manages ac.js::

```
      python manage.py configureac
```

