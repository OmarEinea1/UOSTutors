# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20170504_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.CharField(max_length=25, null=True),
        ),
    ]