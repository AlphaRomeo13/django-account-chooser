from account_chooser.settings import ACCOUNT_CHOOSER_SETTINGS as ac_settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class AccountChooserMiddleware(object):
    '''
    intercept any successful signin or signup, allow accountchooser to store
    the account then redirects back to the default redirect url
    '''
    def process_response(self, request, response):
        if request.path in [ac_settings['loginUrl'], ac_settings['signupUrl']]:
            if isinstance(response, HttpResponseRedirect):
                redirect_to = response.get('Location', None)
                url = reverse('account_chooser_store_account')
                url + "/?next={next}".format(next=redirect_to)
                return HttpResponseRedirect(url)
        return response
