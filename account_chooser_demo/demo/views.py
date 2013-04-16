# Create your views here.
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.utils import simplejson as json
from django.conf import settings
import tweepy


def index(request):
    return render(request, "demo/index.html")


def facebook_signup(request):
    return render(request, "demo/facebook_signup.html")


def twitter_signup(request):    
    return render(request, "demo/twitter_signup.html")

def profile(request):
	return render(request, 'demo/yah.html')


def twitter_auth(request):
    consumer_key = settings.CONSTUMER_KEY
    consumer_secret = settings.CONSTUMER_SECRET
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    return HttpResponseRedirect(auth_url)


# def finish_auth(request):
#     consumer_key = "v8wsuWmpbmoKX7IPfEr49A"
#     consumer_secret = "CcoXqIKiyXXzapOKQ8Rq2QBT8NSPU9GpMzTtaiCZs"
#     access_token = settings.ACCESS_TOKEN
#     access_secret = settings.ACCESS_SECRET
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_url)
#     token = request.session.get('request_token')
#     session.delete('request_token')
# 	user = auth.set_request_token(token[0], token[1])


# auth.set_access_token(access_token,access_secret)
# token = request.session.get('request_token')
# print token
# session.delete('request_token')
# first_token = token[0]
# second_token = token[1]
# auth.set_request_token(first_token, second_token)
# try:
#     auth.get_access_token(verifier)
# except tweepy.TweepError:
#     print 'Error! Failed to get access token.'





class Index (TemplateView):
    template_name = 'demo/index.html'
