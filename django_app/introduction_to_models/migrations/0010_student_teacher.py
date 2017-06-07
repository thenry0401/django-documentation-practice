# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0009_auto_20170607_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('home_group', models.CharField(max_length=5)),
                ('cars', models.ManyToManyField(related_name='introduction_to_models_student_related', related_query_name='introduction_to_models_students', to='introduction_to_models.Car')),
            ],
            options={
                'db_table': 'introduction_to_model_abc_student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cls', models.CharField(max_length=20)),
                ('cars', models.ManyToManyField(related_name='introduction_to_models_teacher_related', related_query_name='introduction_to_models_teachers', to='introduction_to_models.Car')),
            ],
            options={
                'db_table': 'introduction_to_models_abc_teacher',
            },
        ),
    ]
