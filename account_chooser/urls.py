from django.conf.urls import patterns, url
from account_chooser.views import UserStatus, StoreAccount

urlpatterns = patterns('account_chooser.views',
                url('^user_status/$', UserStatus.as_view(),
                    name='account_chooser_get_user_status'),
                url('store_account', StoreAccount.as_view(),
                    name='account_chooser_store_account')
                        )
