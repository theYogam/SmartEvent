from django.db import models

# Create your models here.
from django.db import models

from ikwen.core.models import Model, Country, Application


class Participant(Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    opinion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Event(Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title
