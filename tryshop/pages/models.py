from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    types = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    category = models.ForeignKey(Category, blank=True, null=True)

    class Meta:
        ordering = ('types',)
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __unicode__(self):
        return self.title

