from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    ordering = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

class Page(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    ordering = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    category = models.ForeignKey(Category, blank=True, null=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __unicode__(self):
        return self.title

