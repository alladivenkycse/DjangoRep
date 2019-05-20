from django.conf.urls import url
from django.contrib import admin
#from fstapp import views as v1
#from secondapp import views as v2
from firstapp  import views

urlpatterns = [
    url(r'^helloworld/',views.helloWorld),
    url(r'^first/',views.first_view),
    url(r'^second/',views.second_view),
    url(r'^third/',views.third_view),
    ]
