# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 22:24
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_thumbnail_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location=b'/Users/rommelrico/Documents/github/play/python/DigitalMarketplace/static_cdn/protected'), upload_to=products.models.download_media_location),
        ),
    ]
