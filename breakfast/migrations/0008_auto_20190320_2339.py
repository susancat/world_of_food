# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakfast', '0007_auto_20190320_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images'),
        ),
    ]
