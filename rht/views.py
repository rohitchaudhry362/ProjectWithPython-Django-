from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import datetime
# Create your views here.


def index_view(request):
    today = datetime.datetime.now().date()
    strwelcome="Welcome Admin and today is ",today
    return HttpResponse(strwelcome)
