from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    item_in_stock = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    images = models.ImageField(upload_to='product/%Y/%m/%d', blank=True, null=True)

    category = models.ForeignKey(Category, blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        return self.title

class Order(models.Model):
    detail = models.TextField(blank=True)

    user = models.ForeignKey(User, blank=True, null=True)
    product = models.ForeignKey(Product, blank=True, null=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        pass

