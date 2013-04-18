# Create your views here.
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.conf import settings
import tweepy
from django.shortcuts import render
#from requests.sessions import session


class Index (TemplateView):
    template_name = 'demo/index.html'


# handle gplus authontication
#def gplus_signup(request):
#    return render(request,'demo/gplus.html')

# handling twitter authontication 
#def twitter_signup(request):
#    return render(request, "demo/twitter_signup.html")


def twitter_auth(request):
    consumer_key = settings.CONSTUMER_KEY
    consumer_secret = settings.CONSTUMER_SECRET
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    return HttpResponseRedirect(auth_url)


#def twitter_callback(request):
#    auth = tweepy.OAuthHandler(settings.CONSTUMER_KEY, settings.CONSTUMER_SECRET)
#    token = session.get('request_token')
#    session.delete('request_token')
#    auth.set_request_token(token[0], token[1])
#    try:
#        auth.get_access_token(verifier)
#    except tweepy.TweepError:
#        print 'Error! Failed to get access token.'
#    key = auth.access_token.key
#    secret = auth.access_token.secret
#    context = {"key":key, "secret": secret }
#    return render(request,'demo/success_twitter.html',context)
#    # uncomment the next 2 lines rebuild the user session with twitter
#    # auth.set_access_token(key, secret)
#    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#    # api = tweepy.API(auth)
