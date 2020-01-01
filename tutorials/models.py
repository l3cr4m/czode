from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Language(models.Model):
    lang = models.CharField(max_length=30, blank=True, unique=True, null=True)
    logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.lang


class Tutorial(models.Model):
    name = models.CharField(max_length=30, blank=True, unique=True, null=True)
    lname = models.CharField(max_length=30, blank=True, unique=True, null=True)
    billboard = models.ImageField(null=True, blank=True)
    description = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.name

    def short_description(self):
        return self.description[:100] + "..."


class Part(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    slug = models.IntegerField(blank=True, null=True)
    billboard = models.ImageField(null=True, blank=True)
    description = models.TextField()
    #content = models.TextField()
    #content = RichTextField(null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True, config_name='special')
    date = models.DateTimeField(default=timezone.now)

    tutorial = models.ForeignKey(Tutorial, on_delete=models.PROTECT, default=1)

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return self.tutorial.name + " | " + self.name

    def previous(self):
        return self.slug-1

    def next(self):
        return self.slug+1

    def short_description(self):
        return self.description[:300] + "..."
