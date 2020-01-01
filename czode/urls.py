from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include

from . import views
from .views import Homepage
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from tutorials.models import Language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', ListView.as_view(template_name="homepage.html", model=Language), name='home'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('tutorials/', include("tutorials.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
