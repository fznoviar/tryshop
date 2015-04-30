# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(blank=True, to='pages.Category', null=True),
        ),
    ]
