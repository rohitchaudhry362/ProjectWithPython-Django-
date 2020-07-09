from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

def index(request):
    return HttpResponse("hello guys")
