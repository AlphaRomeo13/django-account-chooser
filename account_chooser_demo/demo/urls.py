from django.conf.urls import patterns, url
from demo.views import index, facebook_signup, twitter_signup, twitter_auth, twitter_callback,gplus_signup

urlpatterns = patterns('account_chooser.views',
    url(r'index/$', index, name='demo_index'),
    url(r'facebook/$', facebook_signup, name='demo_facebook'),
    url(r'twitter/$', twitter_signup, name='demo_twitter'),
    url(r'gplus/$', gplus_signup, name='demo_twitter'),
    url(r'twitter_auth/$', twitter_auth, name='demo_twitter'),
    url(r'twitter_callback/$', twitter_callback, name='demo_twitter'),

)
