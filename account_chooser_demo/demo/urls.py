from django.conf.urls import patterns, url
from demo.views import Index

urlpatterns = patterns('account_chooser.views',
    url(r'^$', Index.as_view(),
        name='demo_index'),
)
