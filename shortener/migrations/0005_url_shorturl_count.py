# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-02 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20170601_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='url_shorturl',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
