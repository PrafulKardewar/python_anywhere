
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from newurls import views as v3



urlpatterns = [

    path('datetime_url/',v3.datetimeinfo)

]

