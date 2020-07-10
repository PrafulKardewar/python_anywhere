from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import datetime

#view function get req and respond a responce
#and for every view function we must provide url pattern by using this end user can send a msg
def welcome(request):
    s='<h1>  hello welcome to durga institute </h1>'
    return HttpResponse(s)

