# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodML', '0009_auto_20171127_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesmonthly',
            name='Apr',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Aug',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Dec',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Feb',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Jan',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Jul',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Jun',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Mar',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Nov',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Oct',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='Sep',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesmonthly',
            name='year',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]