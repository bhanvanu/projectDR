# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodML', '0004_salesmonthly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesmonthly',
            name='Apr',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Aug',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Dec',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Feb',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Jan',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Jul',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Jun',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Mar',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Nov',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Oct',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Sep',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='year',
            field=models.TextField(max_length=30),
        ),
    ]