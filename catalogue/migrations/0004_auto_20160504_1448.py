# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20160503_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.Source'),
        ),
    ]
