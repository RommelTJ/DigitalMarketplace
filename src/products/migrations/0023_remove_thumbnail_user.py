# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20160526_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='user',
        ),
    ]
