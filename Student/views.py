from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from users.views import login1
from Stationary.models import Scategory, Sproduct,StatOrder,StatOrderDetails
from Canteen.models import Ccategory, Cproduct,CatOrder,CatOrderDetails
from Librarian.models import LibraryOrder1,LibOrderDetails1
from users.models import MyUser,Student,card
from Student.models import Documents
from Student.forms import DocForm,MyUserForm1,StudentForm1,UpdateDocForm
from users.forms import MyUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout

@login_required
def logout1(request):
    logout(request)
    return login1(request)


def check_user(request):
    if 'user_role' in request.session and request.session['user_role']=="Student":
        return True
    return False


def StudentHome(request):
    if not check_user(request):
        return HttpResponse(str(request.user)+" user is not allowed to view this page")
    return render(request,'StudentHome.html')

def index(request):
    context={}
    username = request.session['username']
    context['username']=username
    s=MyUser.objects.get(user=username)
    s1=Student.objects.get(user=username)
    print(s1.enroll)
    print(s1.sem)
    print(s1.stream)
    context['data']=s
    context['data1']=s1
    return render(request,'student_home.html',context)



def OrderShowForC(request):
    context={}
    username = request.session['username']
    s1=Student.objects.get(user=username)
    print(s1.enroll)
    context['instance']=CatOrder.objects.filter(UserId=s1.enroll).order_by('-CatOrderId')
    return render(request,'OrderShowForC.html',context)

def DetailOfOrderForC(request):
    context={ }
    CatOrderId = request.GET['CatOrderId']
    print(CatOrderId)
    data=CatOrderDetails.objects.filter(CatOrderId=CatOrderId)
    context['data']=data

    mul=1
    add=0
    for i in data:
        mul=i.Price*i.quantity
        add=add+mul
    context['add']=add
    return render(request,'DetailOfOrderForC.html',context)

def OrderShowForS(request):
    context={}
    username = request.session['username']
    s1=Student.objects.get(user=username)
    print(s1.enroll)
    context['instance']=StatOrder.objects.filter(UserId=s1.enroll).order_by('-StatOrderId')
    return render(request,'OrderShowForS.html',context)

def DetailOfOrderForS(request):
    context={ }
    StatOrderId = request.GET['StatOrderId']
    print(StatOrderId)
    data=StatOrderDetails.objects.filter(StatOrderId=StatOrderId)
    context['data']=data

    mul=1
    add=0
    for i in data:
        mul=i.Price*i.quantity
        add=add+mul
    context['add']=add
    return render(request,'DetailOfOrderForS.html',context)

def OrderShowForL(request):
    context={}
    username = request.session['username']
    s1=Student.objects.get(user=username)
    print(s1.enroll)
    context['instance']=LibraryOrder1.objects.filter(UserId=s1.enroll).order_by('-LibOrderId')
    return render(request,'OrderShowForL.html',context)

def DetailOfOrderForL(request):
    context={ }
    LibOrderId = request.GET['LibOrderId']
    print(LibOrderId)
    data=LibOrderDetails1.objects.filter(LibOrderId=LibOrderId)
    s=LibraryOrder1.objects.get(LibOrderId=LibOrderId)
    context['date']=s.DateOfOrder
    context['data']=data
    return render(request,'DetailOfOrderForL.html',context)

def uploaddoc(request):
    context={}
    if request.method == 'GET':
        username = request.session['username']
        s=Student.objects.get(user=username)
        print(s.enroll)
        if Documents.objects.filter(enroll=s.enroll).exists():
            return render(request,'uploadalready.html')
        else:
            context['object']=s.enroll
            form = DocForm()
    elif request.method == "POST":
        print("here in post request")
        form = DocForm(data=request.POST,files=request.FILES)
        print("here is the data")
        if form.is_valid():
            print("form is valid")
            cat = form.save()

            return HttpResponseRedirect('/Student/index_view/')
    context['form'] = form
    return render(request, 'uploaddoc.html', context)


def updatedoc(request):
    context={}
    if request.method == 'GET':
        username = request.session['username']
        print("hello ", username)
        s1=Student.objects.get(user=username)
        print(s1.enroll)

        instance = Documents.objects.get(enroll=s1.enroll)
        form = UpdateDocForm(instance=instance)
    elif request.method == "POST":
        username = request.session['username']
        print("hello ", username)
        s1=Student.objects.get(user=username)
        print(s1.enroll)
        instance = Documents.objects.get(enroll=s1.enroll)
        form = UpdateDocForm(data=request.POST,files=request.FILES,instance=instance)
        if form.is_valid():
            cat = form.save()
            messages.success(request,"documents updated successfully")
            return HttpResponseRedirect('/Student/updatedoc/')
    context['form'] = form
    return render(request, 'updatedoc.html', context)


def updateprofile(request):
    context={}
    if request.method=='GET':
        username=request.session['username']
        s1=MyUser.objects.get(user=username)
        s2=Student.objects.get(user=username)
        context['enroll']=s2.enroll
        form=MyUserForm1(instance=s1)
    elif request.method=="POST":
        username=request.session['username']
        s1=MyUser.objects.get(user=username)
        form=MyUserForm1(data=request.POST,files=request.FILES,instance=s1)
        if form.is_valid():
            cat=form.save()
            return HttpResponseRedirect('/Student/index_view/')
    context['form']=form
    return render(request,"updateprofile.html",context)

def updatesem(request):
    context = {}
    if request.method =='GET':
        enroll=request.GET['enroll']
        s2=Student.objects.get(enroll=enroll)
        print(s2.sem)
        form1=StudentForm1()
        print(form1)
    elif request.method == "POST":
        enroll=request.GET['enroll']
        s2=Student.objects.get(enroll=enroll)

        form2 = StudentForm1(data=request.POST)
        if form2.is_valid():
            cat1=form2.save()
            return HttpResponseRedirect('/Student/index_view/')
    context['form']=form1
    return render(request,'updatesem1.html',context)

def blockcard(request):
    context={}
    if request.method=="GET":
        username=request.session['username']
        s2=Student.objects.get(user=username)
        s3=card.objects.get(enroll=s2.enroll)
        data=s3.isblocked
        context['data']=data
    elif request.method=="POST":
        username=request.session['username']
        s2=Student.objects.get(user=username)
        s=card.objects.get(enroll=s2.enroll)
        if s.isblocked==True:
            s.isblocked=False
        else:
            s.isblocked=True
        s.save()
        if s.isblocked==True:
            messages.warning(request,"card is blocked")
        else:
            messages.success(request,"card is unblocked")
        return HttpResponseRedirect('/Student/index_view/')

    return render(request,"cardblock.html",context)
