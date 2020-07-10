from django.shortcuts import render
from django.http import HttpResponse
import datetime
date=datetime.datetime.now()
print(date)



def datetimeinfo(request):
    date=datetime.datetime.now()

    my_dict={'temp':date}
    return render(request,'datetimeapp/wish.html',context=my_dict)



