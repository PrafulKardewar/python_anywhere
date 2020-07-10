from django.shortcuts import render
from django.http import HttpResponse
import datetime


def datetimeinfo(request):
    date1=datetime.datetime.now()
    h=int(date1.strftime('%H'))
    msg='<h2> Hello durga a very'

    if h<12:
        msg=msg+'good morning'
    if h<16:
        msg=msg+'good afternoon'
    if h<21:
        msg=msg+'good evening'
    msg=msg+'</h2><hr>'
    msg=msg+'<h2> The current DateTime is  '+str(date1)+'</h2>'
    return HttpResponse(msg)






