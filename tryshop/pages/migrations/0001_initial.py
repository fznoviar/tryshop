# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('types', models.CharField(max_length=255)),
                ('short_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('order', models.IntegerField(default=0)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('types',),
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
