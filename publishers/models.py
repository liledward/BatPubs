from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from bs4 import BeautifulSoup
import requests
import re
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=120, unique=True)
    category = models.ForeignKey(Category)
    description = models.TextField(max_length=600)
    website_address = models.URLField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, unique=True)
    popularity_rank = models.CharField(max_length=120, default=None, null=True)
    traffic = models.IntegerField(default=None, null=True)

    def save(self, *args, **kwargs):
        full_url = self.website_address
        url = re.compile(r"https?://(www\.)?")
        url = url.sub('', full_url).strip().strip('/')
        alexia_url = 'http://data.alexa.com/data?cli=10&dat=s&url=' + url
        html_doc = requests.get(alexia_url)
        data = html_doc.text
        soup = BeautifulSoup(data, 'xml')
        try:
            add = soup.find("POPULARITY")['TEXT']
            self.traffic = int(add)
        except:
            self.traffic = None

        super(Publisher, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def p_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(p_pre_save_receiver, sender=Publisher)
pre_save.connect(p_pre_save_receiver, sender=Category)
