from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'main/home.html' 
    login_url = '/admin'
