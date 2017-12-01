# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render
from .models import SalesMonthly,Dashboard_daily_sales
from django.http import HttpResponse
from cmpe195.settings import PROJECT_ROOT
import os
import operator
import datetime
import json

# these definitions are used in urls.py file
def index(request):
    return render(request, 'foodML/index.html')

def home_page_view(request):
    today = datetime.datetime.now().date()
    today = ['de','var','shi']
    nottoday = ['r','o']
    return render(request, 'foodML/index.html', {"today" : today},{"not" : nottoday})

def about_page_view(request):
    print dir(SalesMonthly.objects)
    query_results = SalesMonthly.objects.all()

    hourly_curr_array = []
    hourly_prev_array = []
    query_results = Dashboard_daily_sales.objects.all()

    hourly_curr_array, hourly_prev_array = display_hourly_sales(query_results,hourly_curr_array,hourly_prev_array)
    json_hourly_curr = json.dumps(hourly_curr_array)
    json_hourly_prev = json.dumps(hourly_prev_array)

    print(len(hourly_prev_array))
    print(len(hourly_curr_array))


    return render(request, 'foodML/about.html',{"obj": query_results,"hourly_curr":json_hourly_curr,"hourly_prev":json_hourly_prev})

def dashboard_page_view(request):
    hourly_curr_array = []
    hourly_prev_array = []
    test_arr = [1520.26, 1800.43, 2294.67, 1701.88, 2544.83, 3090.44]
    test_arr = json.dumps(test_arr)
    query_results = Dashboard_daily_sales.objects.all()
    menu_top_selling = top_item_dash()
    sales_value = daily_sales_dash(query_results)
    hourly_curr_array, hourly_prev_array = display_hourly_sales(query_results,hourly_curr_array,hourly_prev_array)
    json_hourly_curr = json.dumps(hourly_curr_array)
    json_hourly_prev = json.dumps(hourly_prev_array)

    # print(menu_dict)
    return render(request,'foodML/dashboard.html',{"top": menu_top_selling,"sales":sales_value,"hourly_curr":json_hourly_curr,"hourly_prev":json_hourly_prev,"test_arr":test_arr})

def analytics_page_view(request):
    query_results = SalesMonthly.objects.all()
    analytics_sales_arr = []
    analytics_sales_arr = analytics_sales_prediction(query_results,analytics_sales_arr)
    print(len(analytics_sales_arr))
    return render(request,'foodML/analytics.html',{"analytics_sales":analytics_sales_arr})

def futureworks_page_view(request):
    return render(request,'foodML/futureworks.html')

def top_item_dash():
    menu_dict = {}
    with open(os.path.join(PROJECT_ROOT, 'menu.txt')) as f:
        for line in f:
            line = line.rstrip('\n')
            if line in menu_dict:
                menu_dict[line] = int(menu_dict[line]) + 1
            else:
                menu_dict[line] = '0'
    # print(menu_dict)
    return max(menu_dict.iteritems(), key=operator.itemgetter(1))[0]



def daily_sales_dash(query_results):
    currentDT = datetime.date.today()
    currentTime = datetime.datetime.now().time()
    print(currentTime)
    parsed__time = parseTime(currentTime)
    parsed__time = '15' ## remember to remove this --hardcoded
    print (dir(query_results))
    for row in query_results:
        #if row equals current time and date
        if str(row.Date) == str(currentDT):
            print('date equals')
            if parsed__time < '12':
                break

            elif parsed__time >= '12' and parsed__time < '14':
                sales_value = int(row.ten_to_twelve)
                break

            elif parsed__time >= '14' and parsed__time < '16':
                sales_value = float(row.ten_to_twelve) + float(row.twelve_to_fourteen)
                print(sales_value)
                break

            elif parsed__time >= '16' and parsed__time < '18':
                sales_value = float(row.ten_to_twelve) + float(row.twelve_to_fourteen) + float(row.fourteen_to_sixteen )
                break

            elif parsed__time >= '18' and parsed__time < '20':
                sales_value = float(row.ten_to_twelve) + float(row.twelve_to_fourteen)+ float(row.fourteen_to_sixteen ) + float(row.sixteen_to_eighteen)
                break

            elif parsed__time >= '20' and parsed__time < '22':
                sales_value = float(row.ten_to_twelve) + float(row.twelve_to_fourteen) + float(row.fourteen_to_sixteen )+ float(row.sixteen_to_eighteen) + float(row.eighteen_to_twenty )
                break

            elif parsed__time > '22':
                sales_value = float(row.ten_to_twelve) + float(row.twelve_to_fourteen) + float(row.fourteen_to_sixteen ) + float(row.sixteen_to_eighteen) + float(row.eighteen_to_twenty ) + float(row.twenty_to_twentytwo)
                break

            else:
                pass
        else:
            sales_value = 5026.99
    return sales_value


def parseTime(curr_time):
    return str(curr_time).split(':')[0]

def display_hourly_sales(query_results,hourly_curr_array, hourly_prev_array):
    for i, row in enumerate(query_results):
        if i == 0:
            hourly_curr_array = append_array(hourly_curr_array,row)
        if i == 1:
            hourly_prev_array = append_array(hourly_prev_array,row)
            break
    return hourly_curr_array, hourly_prev_array


def append_array(arr,row):
    arr.append(float(row.ten_to_twelve))
    arr.append(float(row.twelve_to_fourteen))
    arr.append(float(row.fourteen_to_sixteen))
    arr.append(float(row.sixteen_to_eighteen))
    arr.append(float(row.eighteen_to_twenty))
    arr.append(float(row.twenty_to_twentytwo))

    return arr

def analytics_sales_prediction(query_results,analytics_sales_arr):
    print(query_results)

    for i, row in enumerate(query_results):
        if i >= 3:
            break
        else:
            analytics_sales_arr = append_array_analytics(analytics_sales_arr,row)
    print("=====================================================================")
    print(analytics_sales_arr)
    return analytics_sales_arr


def append_array_analytics(analytics_sales_arr,row):

    analytics_sales_arr.append(float(row.Jan))
    analytics_sales_arr.append(float(row.Feb))
    analytics_sales_arr.append(float(row.Mar))
    analytics_sales_arr.append(float(row.Apr))
    analytics_sales_arr.append(float(row.Jun))
    analytics_sales_arr.append(float(row.Jul))
    analytics_sales_arr.append(float(row.Aug))
    analytics_sales_arr.append(float(row.Sep))
    analytics_sales_arr.append(float(row.Oct))
    analytics_sales_arr.append(float(row.Nov))
    analytics_sales_arr.append(float(row.Dec))

    return analytics_sales_arr







# Create your views here.
