# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganagroapp', '0009_auto_20170618_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default='trinidad', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
