# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganagroapp', '0014_auto_20170623_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
    ]
