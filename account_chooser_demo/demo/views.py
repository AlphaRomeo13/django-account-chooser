# Create your views here.
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.utils import simplejson as json


class Index (TemplateView):
    template_name = 'demo/index.html'