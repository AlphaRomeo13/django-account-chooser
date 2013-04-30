from account_chooser.settings import ACCOUNT_CHOOSER_SETTINGS as ac_settings
from django.test.utils import setup_test_environment

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.unittest.case import skipIf


class BaseViewTestCase(TestCase):

    fixtures = ('user_testdata',)

    def __init__(self, methodName='runTest'):
        TestCase.__init__(self, methodName=methodName)
        setup_test_environment()
        self.client = Client()

    def _test_url_mapping(self):
        func = resolve(self.URL).func
        func_name = '{}.{}'.format(func.__module__, func.__name__)
        self.assertEquals(self.VIEW_PATH, func_name)


class AccountChooserMiddleWaretest(BaseViewTestCase):

    def setUp(self):
        BaseViewTestCase.setUp(self)
        self.user = User.objects.get(username='registered')

    def test_redirect_after_login(self):
        post_data = {'username': self.user.username,
                     'password': '123',
                     }
        response = self.client.post(getattr(settings, 'LOGIN_URL'),
                                                data=post_data, follow=True)
        self.assertEqual(response.redirect_chain[0],
                         ('http://testserver/accounts/store_account', 302))
        self.assertEqual(response.context['next'],
                         getattr(settings, 'LOGIN_REDIRECT_URL'))
        self.assertEqual(response.template_name,
                         'account_chooser/store_account.html')

    def test_login_get(self):
        response = self.client.get(getattr(settings, 'LOGIN_URL'))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.template_name,
                            'account_chooser/store_account.html')

#     def test_redirect_after_signup(self):
#         post_data = {'username': 'temporary',
#                      'email': 'temporary@example.com',
#                      'password1': '123',
#                      'password2': '123'
#                      }
#         response = self.client.post(ac_settings["signupUrl"],
#                                                 data=post_data, follow=True)
#         self.assertEqual(response.redirect_chain[0],
#                          ('http://testserver/accounts/store_account', 302))
#         self.assertEqual(response.context['next'],
#                          getattr(settings, 'LOGIN_REDIRECT_URL'))
