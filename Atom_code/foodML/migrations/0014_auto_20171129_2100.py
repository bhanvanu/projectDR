# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodML', '0013_restaurant_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesmonthly',
            name='Year',
            field=models.CharField(max_length=30),
        ),
    ]
