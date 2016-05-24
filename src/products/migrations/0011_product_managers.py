# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 14:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='managers',
            field=models.ManyToManyField(related_name='managers_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
