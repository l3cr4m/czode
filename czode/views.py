from django.shortcuts import render

from django.views.generic import ListView
from tutorials.models import Language

class Homepage(ListView):
    model = Language
    template_name="homepage.html"
