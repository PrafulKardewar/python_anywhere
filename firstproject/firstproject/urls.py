
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from firstapp import views as v1
from datetimeapp import views as v2




urlpatterns = [

    path('admin/', admin.site.urls),
    path('wel/', v1.welcome),
    path('datetime/',v2.datetimeinfo),
    path('newurls/', include('newurls.urls'))
]
