# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakfast', '0009_auto_20190320_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]