# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodML', '0007_auto_20171127_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard_daily_sales',
            name='Date',
            field=models.TextField(max_length=30),
        ),
    ]