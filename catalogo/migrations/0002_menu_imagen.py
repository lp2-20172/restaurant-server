# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='imagen',
            field=models.ImageField(default=2, upload_to='photos/'),
            preserve_default=False,
        ),
    ]
