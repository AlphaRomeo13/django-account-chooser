from account_chooser.settings import ACCOUNT_CHOOSER_SETTINGS as ac_settings
from django.test import TestCase
from django.test.client import Client


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

	def corrent_redirect_test(self):
		login_response = self.client.get(ac_settings["loginUrl"])
		signup_response = self.client.get(ac_settings["signupUrl"])
		login_next = response.get('Location', None)
		signup_next = response.get('Location', None)
		self.assertNotEqual(login_next,None)
		self.assertNotEqual(signup_next,None)
