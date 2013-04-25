import os
from django.test import TestCase
from django.conf import settings
from django.template.loader import get_template
from django.template.context import Context
from account_chooser.settings import ACCOUNT_CHOOSER_SETTINGS
from django.core.management import call_command


class ManagementCommandTest(TestCase):

    def test_configureac_command(self):
        call_command('configureac')
        _context = Context(ACCOUNT_CHOOSER_SETTINGS)
        template = get_template('account_chooser/djac-conf.txt')
        prepared_data = template.render(_context)
        path_to_app = os.path.abspath(os.path.join(os.path.dirname(__file__), '/'.join([os.path.pardir, os.path.pardir])))
        js_file = open(path_to_app + '/account_chooser/static/js/djac-config.js', 'r').read()
        self.assertEqual(prepared_data,js_file)


class GetAccountChooserSettingsTest(TestCase):


	def test_update_default_settings(self):
		for key in ACCOUNT_CHOOSER_SETTINGS.keys():
			if key in settings.ACCOUNT_CHOOSER_SETTINGS:
				self.assertEqual(ACCOUNT_CHOOSER_SETTINGS[key],settings.ACCOUNT_CHOOSER_SETTINGS[key])



class SocialKeysTest(TestCase):


	def test_facebook_settings(self):
		self.assertIsNotNone(settings.FACEBOOK_APP_ID)
		self.assertIsNotNone(settings.FACEBOOK_APP_SECRET)
		self.assertIsNotNone(settings.FACEBOOK_REGISTRATION_BACKEND)
		
		self.assertNotEqual(len(settings.FACEBOOK_APP_ID),0)
		self.assertNotEqual(len(settings.FACEBOOK_APP_SECRET),0)
		self.assertNotEqual(len(settings.FACEBOOK_REGISTRATION_BACKEND),0)
			
	def test_twitter_settings(self):
		self.assertIsNotNone(settings.CONSTUMER_KEY)
		self.assertIsNotNone(settings.CONSTUMER_SECRET)
		self.assertIsNotNone(settings.ACCESS_TOKEN)
		self.assertIsNotNone(settings.ACCESS_SECRET)
		self.assertIsNotNone(settings.CALLBACK)

		self.assertNotEqual(len(settings.CONSTUMER_KEY),0)
		self.assertNotEqual(len(settings.CONSTUMER_SECRET),0)
		self.assertNotEqual(len(settings.ACCESS_TOKEN),0)
		self.assertNotEqual(len(settings.ACCESS_SECRET),0)
		self.assertNotEqual(len(settings.CALLBACK),0)
	
	def test_gplus_settings(self):
		self.assertIsNotNone(settings.CLIENT_ID)
		self.assertIsNotNone(settings.CLIENT_SECRET)
		self.assertIsNotNone(settings.SCOPE)
		self.assertIsNotNone(settings.REDIRECT_URI)
		
		self.assertNotEqual(len(settings.CLIENT_ID),0)
		self.assertNotEqual(len(settings.CLIENT_SECRET),0)
		self.assertNotEqual(len(settings.SCOPE),0)
		self.assertNotEqual(len(settings.REDIRECT_URI),0)

	def test_account_chooser_settings(self):
		self.assertIsNotNone(settings.ACCOUNT_CHOOSER_SETTINGS)
		self.assertIsNotNone(settings.ACCOUNT_CHOOSER_SETTINGS["signupUrl"])
		self.assertIsNotNone(settings.ACCOUNT_CHOOSER_SETTINGS["siteEmailId"])
		self.assertIsNotNone(settings.ACCOUNT_CHOOSER_SETTINGS["sitePasswordId"])
		self.assertIsNotNone(settings.ACCOUNT_CHOOSER_SETTINGS["siteDisplayNameId"])

		self.assertNotEqual(len(settings.ACCOUNT_CHOOSER_SETTINGS),0)
		self.assertNotEqual(len(settings.ACCOUNT_CHOOSER_SETTINGS["signupUrl"]),0)
		self.assertNotEqual(len(settings.ACCOUNT_CHOOSER_SETTINGS["siteEmailId"]),0)
		self.assertNotEqual(len(settings.ACCOUNT_CHOOSER_SETTINGS["sitePasswordId"]),0)
		self.assertNotEqual(len(settings.ACCOUNT_CHOOSER_SETTINGS["siteDisplayNameId"]),0)

# self.assertEqual(ac_settings[0]["signupUrl"],settings.ACCOUNT_CHOOSER_SETTINGS["signupUrl"])
# self.assertEqual(ac_settings[0]["siteEmailId"],settings.ACCOUNT_CHOOSER_SETTINGS["siteEmailId"])
# self.assertEqual(ac_settings[0]["sitePasswordId"],settings.ACCOUNT_CHOOSER_SETTINGS["sitePasswordId"])
# self.assertEqual(ac_settings[0]["siteDisplayNameId"],settings.ACCOUNT_CHOOSER_SETTINGS["siteDisplayNameId"])
# self.assertEqual(ac_settings[0]["providers"],settings.ACCOUNT_CHOOSER_SETTINGS["providers"])
