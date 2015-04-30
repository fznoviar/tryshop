# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('short_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('picture', models.ImageField(null=True, upload_to=b'product/%Y/%m/%d', blank=True)),
                ('category', models.ForeignKey(blank=True, to='product.Category', null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
