from django.conf.urls import patterns, url
from demo.views import Index

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='demo_index'),
#    url(r'facebook/$', facebook_signup, name='demo_facebook'),
#    url(r'twitter/$', twitter_signup, name='demo_twitter'),
    url(r'twitter_auth/$', 'demo.views.twitter_auth', name='demo_twitter'),
    url(r'gplus_auth/$', 'demo.views.gplus_auth', name='demo_gplus'),
    url(r'twitter_callback/$', 'demo.views.twitter_callback', name='twitter_callback'),
    url(r'gplus_callback/$', 'demo.views.gplus_callback', name='gplus_callback'),
)
