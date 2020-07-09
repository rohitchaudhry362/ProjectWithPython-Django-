from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from users.models import Role,UserProfile,MyUser,Student,card,mobile
from users.forms import MyUserForm,UserProfileForm,StudentForm,MobileForm
from django.contrib import messages
import requests
import random


def index_view(request):
    today = datetime.datetime.now().date()
    strwelcome="Welcome Admin and today is ",today
    return HttpResponse(strwelcome)
#____________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________--
def login1(request):
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            print(username," --- ",raw_password)
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            s=MyUser.objects.get(user=username)
            print('Hellobro')
            print(s.user)
            request.session['username']=s.user


            if s.uniqueid==111111111111:
                return HttpResponseRedirect('/Canteen/')
            if s.uniqueid==222222222222:
                return HttpResponseRedirect('/Stationary/')
            if s.uniqueid==333333333333:
                return HttpResponseRedirect('/Librarian/')
            if s.uniqueid==444444444444:
                return HttpResponseRedirect('/Student/index_view/')
            if s.uniqueid==555555555555:
                return HttpResponseRedirect('/myadmin/')
    else:

        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method=='POST':
        form=UserCreationForm(data=request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("here is the data")
            print(username)
            request.session['username']=username
            return HttpResponseRedirect('/users/signup/')
    else:
        form=UserCreationForm()
        context={'form':form}
        return render(request,'reg_form.html',context)



def registration1(request):
    context={}
    if request.method=='POST':
        form = MyUserForm(data=request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            uniqueid=form.cleaned_data.get('uniqueid')
            print(uniqueid)
            if uniqueid==444444444444:
                return HttpResponseRedirect('/users/studentdetail/')
            else:
                messages.success(request,"You've been successfully registered!!")
                return HttpResponseRedirect('/users/login1/')
        else:
            messages.error(request,"Submit the data as per requirement!!")
            username=request.session['username']
            form = MyUserForm()
            context['username']=username
            context['form']=form
            return render(request, 'reg_form1.html', context)

    else:
        username=request.session['username']
        print("this is session")
        print(username)
        form = MyUserForm()
        context['username']=username
        context['form']=form
    return render(request, 'reg_form1.html', context)

def studentdetail(request):
    context={}
    context={}
    if request.method=='POST':
        form = StudentForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            enrollment = form.cleaned_data.get('enroll')
            print("hey buddy ")
            print(enrollment)
            messages.success(request,"You've been successfully registered!!")
            s=card()
            s.enroll=enrollment
            s.isblocked=False
            s.save()
            return HttpResponseRedirect('/users/login1/')
    else:
        username=request.session['username']
        form=StudentForm()
        context['username']=username
        context['form']=form
    return render(request,"studentdetail.html",context)

def mobilenumber(request):
    context={}
    if request.method=='POST':
        print("this is post request")
        form = MobileForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            mobilenumber = form.cleaned_data.get('mobilenumber')
            request.session['mobilenumber']=mobilenumber
            if MyUser.objects.filter(phone_number=mobilenumber).exists():
                print("sending msg initiated")
                return sendsms(request)
            else:
                messages.warning(request,"enter valid mobile number")
                return HttpResponseRedirect('/users/mobilenumber/')
    else:
        form=MobileForm()
        context['form']=form
    return render(request,"mobilenumber.html",context)



def sendsms(request):
    otp=random.randint(111111,999999)
    print(otp)
    mobilenumber=request.session['mobilenumber']
    s=mobile.objects.latest()
    s.otp=otp
    s.save()
    mobilenumber1=str(mobilenumber)
    mn=mobilenumber1[3:]
    print(mn)

    url = "https://smsapi.engineeringtgr.com/send/"

    params = dict(
        Mobile='8264327271',
        Password='Iamrht362@',
        Key='rohity1TUrdf6wi2LA35FYo07m',
        Message=otp,
        To="8264327271")

    resp = requests.get(url, params)
    print(resp, resp.text)
