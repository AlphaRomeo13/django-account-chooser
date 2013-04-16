from django.conf.urls import patterns, url
from account_chooser.views import UserStatus
from demo.views import profile
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('account_chooser.views',
                        url('^user_status/$', csrf_exempt(UserStatus.as_view()), name='account_chooser_get_user_status'),
                        url(r'profile/$', profile),

                        )
