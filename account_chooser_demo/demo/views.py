# Create your views here.
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.contrib.admindocs.views import extract_views_from_urlpatterns, \
    simplify_regex

from oauth2client.client import OAuth2WebServerFlow
import tweepy
from oauth2client.file import Storage

# from requests.sessions import session


class Index (TemplateView):
    template_name = 'demo/index.html'

    def _get_urls(self):
        urls = []
        if settings.ADMIN_FOR:
            settings_modules = [__import__(m, {}, {}, ['']) for m in settings.ADMIN_FOR]
        else:
            settings_modules = [settings]

        for settings_mod in settings_modules:
            try:
                urlconf = __import__(settings_mod.ROOT_URLCONF, {}, {}, [''])
            except Exception as e:
                continue
            view_functions = extract_views_from_urlpatterns(urlconf.urlpatterns)
            for view_function in view_functions:
                urls.append(simplify_regex(view_function[1]))
        return urls

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['url_list'] = self._get_urls()
        return context


def twitter_auth(request):
    consumer_key = settings.CONSTUMER_KEY
    consumer_secret = settings.CONSTUMER_SECRET
    call_back = "http://account-chooser-demo.herokuapp.com/demo/twitter_callback/"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, call_back)
    auth_url = auth.get_authorization_url()
    return HttpResponseRedirect(auth_url)


def gplus_auth(request):
    flow = OAuth2WebServerFlow(client_id='308413983615.apps.googleusercontent.com',
                           client_secret='GboICNuFvxGbB679f0hUNbRl',
                           scope='https://www.googleapis.com/auth/plus.login',
                           redirect_uri='http://localhost:8000/gplus_callback')
    auth_url = flow.step1_get_authorize_url()
    return HttpResponseRedirect(auth_url)


def twitter_callback(request):
    call_back = "http://account-chooser-demo.herokuapp.com/demo/twitter_callback/"
    auth = tweepy.OAuthHandler(settings.CONSTUMER_KEY, settings.CONSTUMER_SECRET, call_back)
    auth.set_request_token(request.GET['oauth_token'], request.GET['oauth_verifier'])
    auth.get_access_token(request.GET['oauth_verifier'])
    key = auth.access_token.key
    secret = auth.access_token.secret
    context = {'key': key, 'secret': secret}
    return render(request, 'demo/success_twitter.html', context)


def gplus_callback(request):
    flow = OAuth2WebServerFlow(client_id='308413983615.apps.googleusercontent.com',
                           client_secret='GboICNuFvxGbB679f0hUNbRl',
                           scope='https://www.googleapis.com/auth/plus.login',
                           redirect_uri='http://localhost:8000/gplus_callback')

    credentials = flow.step2_exchange(request.GET['code'])

    storage = Storage('testing.txt')  # prepare file to store user info in it
    storage.put(credentials)  # storing user info in file
    context = {"info":  credentials}
    return render(request, 'demo/success_gplus.html', context)
