from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from . models import Tutorial, Part
from django.core.paginator import Paginator
from django.views.generic.list import MultipleObjectMixin


class TutorialList(ListView):
    template_name="tutorial.html"

    def get_queryset(self):
        self.name = get_object_or_404(Tutorial, lname=self.kwargs['tutorial'])
        return Part.objects.filter(tutorial=self.name)

class TutorialDetail(DetailView):
    template_name="part.html"

    def get_queryset(self):
        self.name = get_object_or_404(Tutorial, lname=self.kwargs['tutorial'])
        return Part.objects.filter(tutorial=self.name)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        self.name = get_object_or_404(Tutorial, lname=self.kwargs['tutorial'])
        context['list_count'] = Part.objects.filter(tutorial=self.name)
        return context
