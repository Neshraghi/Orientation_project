# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-03 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='end_date',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='start_date',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='type',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]
