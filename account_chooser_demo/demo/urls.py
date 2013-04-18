from django.conf.urls import patterns, url
from demo.views import Index, twitter_auth

urlpatterns = patterns('account_chooser.views',
#    url(r'index/$', Index.as_view(), name='demo_index'),
#    url(r'facebook/$', facebook_signup, name='demo_facebook'),
#    url(r'twitter/$', twitter_signup, name='demo_twitter'),
    url(r'twitter_auth/$', twitter_auth, name='demo_twitter'),
#    url(r'gplus/$', gplus_signup, name='demo_twitter'),
#    url(r'twitter_callback/$', twitter_callback, name='demo_twitter'),

)
