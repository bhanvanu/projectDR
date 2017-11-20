# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render

from django.http import HttpResponse

# these definitions are used in urls.py file
def index(request):
    return render(request, 'foodML/index.html')

def home_page_view(request):
    today = datetime.datetime.now().date()
    today = ['de','var','shi']
    nottoday = ['r','o']
    return render(request, 'foodML/index.html', {"today" : today},{"not" : nottoday})

def about_page_view(request):
    return render(request, 'foodML/about.html')

def dashboard_page_view(request):
    return render(request,'foodML/dashboard.html')

def analytics_page_view(request):
    return render(request,'foodML/analytics.html')

def futureworks_page_view(request):
    return render(request,'foodML/futureworks.html')

# Create your views here.
