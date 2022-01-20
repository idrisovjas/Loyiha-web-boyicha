from django.shortcuts import render
from django.http import  HttpResponse
from django.views.generic import ListView,TemplateView
from .models import model
# Create your views here.

def jasurbek(request):
    return HttpResponse('salom jasurbek aka sinzni sogindim!')

class sahifaclass(TemplateView):
    template_name = 'sahifa1.html'


class sahifa2class(TemplateView):
    template_name = 'sahifa2.html'

class sahifa3class(TemplateView):
    template_name = 'sahifa3.html'

class bosh(TemplateView):
    template_name = 'asos.html'

class Boshsahifa(ListView):
    model = model
    template_name = 'bbb.html'






