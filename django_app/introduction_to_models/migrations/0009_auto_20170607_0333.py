# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0008_auto_20170607_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='servers_hot_dogs',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='serves_hot_dogs',
            field=models.BooleanField(default=False),
        ),
    ]