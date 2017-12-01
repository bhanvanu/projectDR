# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class SalesMonthly(models.Model):
    Year = models.CharField(max_length=30)
    Jan = models.DecimalField(max_digits=8, decimal_places=2)
    Feb = models.DecimalField(max_digits=8, decimal_places=2)
    Mar = models.DecimalField(max_digits=8, decimal_places=2)
    Apr = models.DecimalField(max_digits=8, decimal_places=2)
    Jun = models.DecimalField(max_digits=8, decimal_places=2)
    Jul = models.DecimalField(max_digits=8, decimal_places=2)
    Aug = models.DecimalField(max_digits=8, decimal_places=2)
    Sep = models.DecimalField(max_digits=8, decimal_places=2)
    Oct = models.DecimalField(max_digits=8, decimal_places=2)
    Nov = models.DecimalField(max_digits=8, decimal_places=2)
    Dec = models.DecimalField(max_digits=8, decimal_places=2)

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=16)

class Dashboard_daily_sales(models.Model):
    Date = models.TextField(max_length=30)
    ten_to_twelve = models.DecimalField(max_digits=8, decimal_places=2)
    twelve_to_fourteen = models.DecimalField(max_digits=8, decimal_places=2)
    fourteen_to_sixteen = models.DecimalField(max_digits=8, decimal_places=2)
    sixteen_to_eighteen = models.DecimalField(max_digits=8, decimal_places=2)
    eighteen_to_twenty = models.DecimalField(max_digits=8, decimal_places=2)
    twenty_to_twentytwo = models.DecimalField(max_digits=8, decimal_places=2)

# Create your models here.
