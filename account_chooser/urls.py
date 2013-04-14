from django.conf.urls import patterns, url
from account_chooser.views import UserStatus

urlpatterns = patterns('account_chooser.views',
                        url('^user_status/$', UserStatus.as_view(),
                            name='account_chooser_get_user_status'),
                        )
