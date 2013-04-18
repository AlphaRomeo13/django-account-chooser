# Create your views here.
from django.views.generic.base import View
from django.http import HttpResponse
from django.utils import simplejson as json
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class UserStatus (View):
    '''
     If the user clicks on one of the accounts, ac.js sends an HTTP POST request
     to this view.
     URL query parameters:
         "email"
         "displayName"
         "photoUrl"
         "providerId"
     return: JSON representing the status of user:
         {"registered":true} means the user is registered, redirect to login
         {"registered":false} means the user is not registered, redirect to signup
         {"authUri":"IP-uri"} means that user relies on an Identity Provider
         and the user should be redirected to the provided IP-uri which
         will start the appropriate federation protocol with that IDP.
         In this case ac.js will dispatch to that URI,
         and the subsequent login path depends on how that provider works.
    '''

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UserStatus, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):

        if 'providerId' in request.POST.keys():
            response_data = {"authUri":"IP-uri"}
        elif User.objects.filter(email=request.POST['email']).exists():
            response_data = {"registered":True}
        else:
            response_data = {"registered":False}
        print response_data
        return HttpResponse(json.dumps(response_data),
                            mimetype="application/json")


class StoreAccount (View):
    '''
    invokes ac.js and uses the storeAccount feature instructing it to
    store the account info. If the login info was provided via AccountChooser,
    this is a fast, efficient no-op.
    '''
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        from account_chooser.settings import ACCOUNT_CHOOSER_SETTINGS
        redirect_to = request.REQUEST.get('next',
                                          ACCOUNT_CHOOSER_SETTINGS['homeUrl'])
        return render(request, 'account_chooser/store_account.html',
                              {'user': request.user,
                               'next': redirect_to})
