# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pallevelugu', '0028_mediupdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='passwd',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
