# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=0, upload_to='img'),
            preserve_default=False,
        ),
    ]
