# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20161026_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='bbrefID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
