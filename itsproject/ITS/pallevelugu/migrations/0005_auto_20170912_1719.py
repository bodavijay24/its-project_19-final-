# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pallevelugu', '0004_auto_20170912_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='households',
            name='Latitude',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='households',
            name='Longitude',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
