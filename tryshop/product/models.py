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

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to='product/%Y/%m/%d', blank=True, null=True)

    category = models.ForeignKey(Category, blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        return self.title


