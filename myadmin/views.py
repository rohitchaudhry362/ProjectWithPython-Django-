from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from users.models import MyUser,Student,Query
from myadmin.forms import StudentForm
from Student.models import Documents


def index(request):
    context={}
    username = request.session['username']
    context['username']=username
    s=MyUser.objects.get(user=username)
    context['data']=s
    return render(request,'myadminhome.html',context)

def studentlist(request):
    context={}
    s=MyUser.objects.all()
    t=Student.objects.all()
    print(t)
    context['s1']=s
    context['t1']=t
    return render(request,'studentlist1.html',context)

def studentprofile(request):
    context={}
    if request.method=="GET":
        enroll=request.GET['enroll']
        context['enroll']=enroll
        print(enroll)
        s=Student.objects.get(enroll=enroll)
        print(s.user)
        t1=MyUser.objects.get(user=s.user)
        context['t']=t1
        return render(request,"studentprofile.html",context)

def updatebalance(request):
    context={}
    if request.method=='GET':
        enroll=request.GET['enroll']
        print(enroll)
        s=Student.objects.get(enroll=enroll)
        print(s)
        form = StudentForm(instance=s)
    elif request.method == "POST":
        enroll=request.GET['enroll']
        s=Student.objects.get(enroll=enroll)
        amount=s.balance
        form = StudentForm(data=request.POST,files=request.FILES,instance=s)
        if form.is_valid():
            cat = form.save()
            messages.success(request,"balance updated successfully")
            s=Student.objects.get(enroll=enroll)
            s.balance=s.balance+amount
            s.save()
            return HttpResponseRedirect('/myadmin/studentlist/')
    context['form'] = form
    return render(request, 'updatebalance.html', context)

def showdocs(request):
    context={}
    enroll=request.GET['enroll']
    s=Documents.objects.get(enroll_id=enroll)
    context["docs"]=s
    return render(request,'showdocs.html',context)

def respondqueries(request):
    context={}
    queries=Query.objects.all()
    print(queries)
    context['queries']=queries
    return render(request,"respondqueries.html",context)

def reviewqueries(request):
    queryid=request.GET['queryid']
    s=Query.objects.get(queryid=queryid)
    s.isreviewed=True
    s.save()
    return HttpResponseRedirect('/myadmin/respondqueries')
