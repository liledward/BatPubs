from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category)
    description = models.TextField(max_length=600)
    website_address = models.URLField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)

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
