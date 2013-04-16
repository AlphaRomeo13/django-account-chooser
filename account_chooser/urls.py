from django.conf.urls import patterns, url
from account_chooser.views import UserStatus, StoreAccount
from demo.views import profile
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('account_chooser.views',
              url(r'^user_status/$', UserStatus.as_view(),
                    name='account_chooser_get_user_status'),
                url(r'store_account', StoreAccount.as_view(),
                    name='account_chooser_store_account')
                url(r'profile/$', profile),
                        )
