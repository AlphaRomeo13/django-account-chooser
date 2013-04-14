from django.conf.urls import patterns, url
# from demo.views import Index
from demo.views import index, facebook_signup, twitter_signup, twitter_auth, yah, gplus_auth

urlpatterns = patterns('account_chooser.views',
							url(r'index/$', index, name='demo_index'),
							url(r'facebook/$', facebook_signup, name='demo_facebook'),
							url(r'twitter/$', twitter_signup, name='demo_twitter'),
							url(r'gplus_auth/$', gplus_auth, name='demo_gplus'),
							url(r'twitter_auth/$', twitter_auth, name='demo_twitter'),
							url(r'yah/$', yah, name='demo_happy'),
						    # url(r'$', Index.as_view(), name='demo_index'),
)
