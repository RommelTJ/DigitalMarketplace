# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20160526_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='type',
            field=models.CharField(choices=[('hd', 'HD'), ('sd', 'SD'), ('micro', 'Micro')], default='hd', max_length=20),
        ),
    ]
