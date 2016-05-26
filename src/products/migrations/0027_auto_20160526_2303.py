# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20160526_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=9.99, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='media',
            field=models.ImageField(blank=True, height_field=b'height', null=True, upload_to=products.models.thumbnail_location, width_field=b'width'),
        ),
    ]
