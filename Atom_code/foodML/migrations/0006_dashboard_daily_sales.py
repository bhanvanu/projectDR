# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodML', '0005_auto_20171120_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard_daily_sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('ten_to_twelve', models.DecimalField(decimal_places=2, max_digits=5)),
                ('twelve_to_fourteen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fourteen_to_sixteen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sixteen_to_eighteen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eighteen_to_twenty', models.DecimalField(decimal_places=2, max_digits=5)),
                ('twenty_to_twentytwo', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]