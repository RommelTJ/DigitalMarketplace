# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 21:36
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0017_auto_20160526_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(blank=True, max_length=20, null=True)),
                ('width', models.CharField(blank=True, max_length=20, null=True)),
                ('media', models.ImageField(blank=True, height_field=models.CharField(blank=True, max_length=20, null=True), null=True, storage=django.core.files.storage.FileSystemStorage(location=b'/Users/rommelrico/Documents/github/play/python/DigitalMarketplace/static_cdn/protected'), upload_to=products.models.download_media_location, width_field=models.CharField(blank=True, max_length=20, null=True))),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
