from django.shortcuts import render
from django.http import HttpResponse
import datetime
def second_view(request):
    return HttpResponse("Alladi Second Application")
