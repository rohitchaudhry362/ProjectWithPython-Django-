from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
#from UserManagement.models import UserRole
import zerosms
from random import randint
from UserManagement.forms import Registrationform


# Create your views here.
def index_view(request):
    today = datetime.datetime.now().date()
    strwelcome="Welcome Admin and today is ",today
    return HttpResponse(strwelcome)

#USerREgistrationForm




def registration(request):
    if request.method=='POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #user_role = UserRole(user=user, role="student")
            #user_role.save()
            login(request, user)
            return HttpResponseRedirect('/UserManagement/profile')

    else:
        form = Registrationform()
    return render(request, 'registration.html', {'form': form})
