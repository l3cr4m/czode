from django.urls import path, re_path
from . views import TutorialList, TutorialDetail

from .models import Tutorial, Part
from django.views.generic.base import TemplateView
from django.views.generic import ListView


app_name = 'tutorials'

urlpatterns = [
    path('', ListView.as_view(template_name="tutorials.html", model=Tutorial), name='tutorials'),
    path('<tutorial>', TutorialList.as_view(), name='tutorial'),
    path('<tutorial>/<int:slug>', TutorialDetail.as_view(), name='part'),
]
