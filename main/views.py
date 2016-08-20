from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class FamilyTvView(TemplateView):
    template_name = 'familytv.html'

class EmilysListView(TemplateView):
    template_name = 'emilyslist.html'

class URLShortenerView(TemplateView):
    template_name = 'emily_url_shortener.html'
