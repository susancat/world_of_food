# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakfast', '0004_auto_20190320_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.CharField(blank=True, default='', max_length=128),
            preserve_default=False,
        ),
    ]
