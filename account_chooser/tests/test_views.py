from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test.client import Client
from django.core.urlresolvers import resolve, reverse
from django.contrib.auth.models import User


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


class UserStatusViewTest(BaseViewTestCase):

    URL = reverse('account_chooser_get_user_status')
    VIEW_PATH = 'account_chooser.views.UserStatus'

    def test_url_mapping(self):
        BaseViewTestCase._test_url_mapping(self)

    def test_GET_request(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 405)

    def test_POST_request(self):

        def test(response, desired):
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get('content-type'), "application/json")
            self.assertEqual(response.content, desired)

        data = {"email": 'mail@example.com',
                "displayName": 'facebook_user',
                "providerId": 'facebook.com'
                }
        test(self.client.post(self.URL, data),
                                        '{"authUri": "/facebook/connect"}')

        data = {"email": 'registered.mail@example.com',
                "displayName": 'registered',
                }
        User.objects.all()
        test(self.client.post(self.URL, data), '{"registered": true}')

        data = {"email": 'notregistered.mail@example.com',
                "displayName": 'notregistered',
                }
        test(self.client.post(self.URL, data), '{"registered": false}')


class StoreAccountViewTest(BaseViewTestCase):

    URL = reverse('account_chooser_store_account')
    VIEW_PATH = 'account_chooser.views.StoreAccount'

    def setUp(self):
        BaseViewTestCase.setUp(self)
        user = User.objects.get(username='registered')
        self.client.login(username=user.username, password='123')

    def test_url_mapping(self):
        BaseViewTestCase._test_url_mapping(self)

    def test_GET_request(self):
        response = self.client.get(self.URL, data={'next': 'target_url'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('account_chooser/store_account.html',
                      map(lambda template: template.name, response.templates))
        self.assertEqual('target_url', response.context['next'])
        self.assertEqual('registered.mail@example.com',
                                                response.context['user'].email)

    def test_POST_request(self):
        response = self.client.post(self.URL)
        self.assertEqual(response.status_code, 405)
