from account_chooser.settings import ACCOUNT_CHOOSER_SETTINGS as s
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class AccountChooserMiddleware(object):
    def process_response(self, request, response):
        if request.path in [s['loginUrl'], s['signupUrl']]:
            if isinstance(response, HttpResponseRedirect):
#                import pdb; pdb.set_trace()
                redirect_to = response.get('Location', None)
                url = reverse('account_chooser_store_account')
                url + "/?next={next}".format(next=redirect_to)
                return HttpResponseRedirect(url)
        return response
