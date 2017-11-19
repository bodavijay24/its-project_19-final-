# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pallevelugu', '0005_auto_20170912_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='households',
            old_name='tid',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='households',
            name='Latitude',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='households',
            name='Longitude',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
