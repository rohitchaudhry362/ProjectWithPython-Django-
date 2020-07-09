from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from Stationary.models import Scategory, Sproduct,CartProduct,StatOrder,StatOrderDetails
from django.contrib import messages
from users.models import MyUser,card,Student
from django.contrib.auth.decorators import login_required
from Stationary.forms import ScategoryForm,SproductForm,ScategoryDelete,SproductDelete,SproductEdit,CartProductForm,SOrderForm,EditCartProduct1,QueryForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login ,logout
from users.views import login1

@login_required
def logout1(request):
    logout(request)
    return login1(request)

@login_required
def index(request):
    context={}
    username = request.session['username']
    context['username']=username
    s=MyUser.objects.get(user=username)
    context['data']=s
    return render(request,'Scategory_home.html',context)

@login_required
def Scategory_index(request):
    context={}
    context['cat']=Scategory.objects.all()
    return render(request,'Scategory_index.html',context)
@login_required
def create_Scategory(request):
    context = {}
    if request.method == 'GET':
        form = ScategoryForm()
    elif request.method == "POST":
        form = ScategoryForm(data=request.POST)
        if form.is_valid():
            cat = form.save()
            messages.success(request, " New Category Added ")
            return HttpResponseRedirect('/Stationary/Scategory_index/')

    context['form'] = form
    return render(request, 'Scategory_create.html', context)

@login_required
def edit_Scategory(request):
    context = {}
    if request.method == 'GET' and 'CatId' in request.GET:
        CatId = request.GET['CatId']
        context['CatId'] = CatId
        instance = Scategory.objects.get(CatId=CatId)
        form = ScategoryForm(instance=instance)

    elif request.method == "POST":
        CatId = request.POST['CatId']
        instance = Scategory.objects.get(CatId=CatId)
        form = ScategoryForm(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"category %s is updated Sucessfully"%pro.CatName)
            return HttpResponseRedirect('/Stationary/Scategory_index/')
    else:
        return HttpResponse("category id is mandaory")
    context['form'] = form
    return render(request, 'Scategory_create.html', context)
@login_required
def EditFromCart(request):
    context={}
    if request.method=='GET' and 'Pid' in request.GET:
        Pid = request.GET['Pid']
        context['Pid']=Pid
        instance=CartProduct.objects.get(Pid=Pid)
        form=EditCartProduct1(instance=instance)
    elif request.method=="POST":
        Pid=request.POST['Pid']
        instance=CartProduct.objects.get(Pid=Pid)
        form=EditCartProduct1(data=request.POST,instance=instance)
        if form.is_valid():
            pro=form.save()
            messages.success(request,"cart updated successfully")
            return HttpResponseRedirect("/Stationary/StationaryCart/")
    else:
        return HttpResponse("product id is mandatory")
    context["form"]=form
    return render(request,"EditFromCart1.html",context)


@login_required
def delete_Scategory(request):
    context = {}
    if request.method == 'GET' and 'CatId' in request.GET:
        CatId = request.GET['CatId']
        instance=Scategory.objects.get(CatId=CatId)
        context['CatId'] = instance
    elif request.method == "POST":
        CatId = request.GET['CatId']
        instance = Scategory.objects.get(CatId=CatId)
        messages.success(request, "Category <strong>%s</strong> is Deleted "%instance.CatName)
        instance.delete()
        return HttpResponseRedirect('/Stationary/Scategory_index')
    else:
        return HttpResponse("category id is mandaory")

    return render(request, 'Scategory_delete.html', context)

@login_required
def Scategory_order(request):
    context={}
    context['cat']=Scategory.objects.all()
    return render(request,'Scategory_order.html',context)

@login_required
def Sproduct_index(request):
    context={}
    context['pro']=Sproduct.objects.all()
    return render(request,"Sproduct_index.html",context)

@login_required
def edit_Sproduct(request):
    context = {}
    if request.method == 'GET' and 'Pid' in request.GET:
        Pid = request.GET['Pid']
        context['Pid'] = Pid
        instance = Sproduct.objects.get(Pid=Pid)
        form = SproductEdit(instance=instance)

    elif request.method == "POST":
        Pid = request.POST['Pid']
        instance = Sproduct.objects.get(Pid=Pid)
        temp=instance.CatId_id
        form = SproductEdit(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"Product '%s' is updated Sucessfully"%pro.PName)
            return HttpResponseRedirect('/Stationary/SproductbyId/?CatId='+str(temp))
    else:
        return HttpResponse("Product id is mandaory")
    context['form'] = form
    return render(request, 'Sproduct_create.html', context)
@login_required
def create_Sproduct(request):
    context = {}
    if request.method == 'GET':
        form = SproductForm()
    elif request.method == "POST":
        form = SproductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,'new product is added successfully')
            Latest=Sproduct.objects.latest()
            got_cat_id=Latest.CatId_id
            return HttpResponseRedirect('/Stationary/SproductbyId/?CatId='+str(got_cat_id))
    context['form']=form
    return render(request, 'Sproduct_create.html', context)

@login_required
def delete_Sproduct(request):
    context = {}
    if request.method == 'GET' and 'Pid' in request.GET:
        Pid = request.GET['Pid']
        instance=Sproduct.objects.get(Pid=Pid)
        context['Pid'] = instance
    elif request.method == "POST":
        Pid = request.GET['Pid']
        instance = Sproduct.objects.get(Pid=Pid)
        temp=instance.CatId_id
        messages.success(request, "product <strong>%s</strong> is Deleted "%instance.PName)
        instance.delete()
        return HttpResponseRedirect('/Stationary/SproductbyId/?CatId='+str(temp))
    else:
        return HttpResponse("product id is mandaory")

    return render(request, 'Sproduct_delete.html', context)

@login_required
def SproductbyId(request):
    context={ }
    CatId = request.GET['CatId']
    CatId1 = Scategory.objects.get(CatId=CatId)
    Cpro1  = CatId1.sproduct_set.all()
    context={
        'CatId1':CatId1,
        'Cpro1':Cpro1,

    }
    return render(request,'SproductbyId.html',context)

@login_required
def Scategory_order_productbyid(request):
    context={ }
    CatId = request.GET['CatId']
    CatId1 = Scategory.objects.get(CatId=CatId)
    Cpro1  = CatId1.sproduct_set.all()
    context={
        'CatId1':CatId1,
        'Cpro1':Cpro1,

    }
    return render(request,'Scategory_order_productbyid.html',context)

@login_required
def OrderDetails(request):
    context = {}
    if request.method == 'GET':
        form = OrderDetailsForm()
    elif request.method == "POST":
        form = OrderDetailsForm(data=request.POST)
        if form.is_valid():
            order = form.save()

            return HttpResponseRedirect('/Stationary/Scategory_index/')
    context['form'] = form
    return render(request, 'Sorder_details.html', context)

@login_required
def CartShow(request):
    context={}
    context['cat']=CartProduct.objects.all()
    s1=CartProduct.objects.all()
    mul=1
    add=0
    for i in s1:
        mul=i.Price*i.quantity
        add=add+mul
        request.session['add']=add
    context['add']=add
    return render(request,'StationaryCart.html',context)

@login_required
def ClearCart(request):
    instance=CartProduct.objects.all()
    instance.delete()
    messages.success(request,"cart is empty now.You can add new products")
    return HttpResponseRedirect('/Stationary/Scategory_order')

@login_required
def productdetail(request):
    if request.method == "GET":
        Pid = request.GET['Pid']
        pro=Sproduct.objects.filter(Pid=Pid)
        #set_views_count("product", request, pro[0])
        template=loader.get_template('productdetail1.html')
        context={
            'pro':pro[0]
        }
        form = CartProductForm()
    elif request.method == "POST":
        form=CartProductForm(data=request.POST)

        if form.is_valid():
            pro=form.save()

            Pid = form.cleaned_data.get('Pid')
            s=CartProduct.objects.filter(Pid=Pid)
            print("hi canteen")
            print(s)
            count=0
            for i in s:
                count=count+1
            print(count)
            if count>1:
                messages.warning(request,"product is already added in the cart.You can add/remove quantity from cart")
                s=CartProduct.objects.latest()
                s.delete()
                return HttpResponseRedirect('/Stationary/StationaryCart/')
            else:
                messages.success(request,' product is added successfully to cart')
                return HttpResponseRedirect('/Stationary/Scategory_order/')
    context['form'] = form
    return HttpResponse(template.render(context,request))

@login_required
def DeleteFromCart(request):
    Pid = request.GET['Pid']
    instance = CartProduct.objects.get(Pid=Pid)
    messages.success(request, "product is deleted from cart")
    instance.delete()
    return HttpResponseRedirect('/Stationary/StationaryCart/')

@login_required
def PlaceOrder(request):
    context={}
    if request.method == "GET":
        #Pid = request.GET['Pid']
        #pro=Cproduct.objects.filter(Pid=Pid)
        #set_views_count("product", request, pro[0])
        template=loader.get_template('PlaceOrder1.html')
        form = SOrderForm()
    elif request.method == "POST":
        form=SOrderForm(data=request.POST)
        if form.is_valid():
            form.save()
            print("this is line 1")
            UserId=form.cleaned_data.get('UserId')


            if card.objects.filter(enroll=UserId).exists():
                s=card.objects.get(enroll=UserId)
                if(s.isblocked==True):
                    instance=StatOrder.objects.latest()
                    instance.delete()
                    messages.warning(request,"card is blocked")
                    return CartShow(request)
                else:
                    add=request.session['add']
                    print("this is the amount to be debited ",add)
                    s1=Student.objects.get(enroll=UserId)
                    if s1.balance>=add:
                        s1.balance=s1.balance-add
                        s1.save()
                        messages.success(request,'entered id succesfully')
                        return DetailOfOrder1(request)
                    else:
                        instance=StatOrder.objects.latest()
                        instance.delete()
                        messages.warning(request,"not sufficient amount in the card")
                        return CartShow(request)
            else:
                instance=StatOrder.objects.latest()
                instance.delete()
                messages.warning(request,"the userid is not registered")
                return CartShow(request)
    context['form'] = form
    return HttpResponse(template.render(context,request))

@login_required
def DetailOfOrder1(request):
    s=StatOrder.objects.latest('StatOrderId')
    print(s.StatOrderId)
    r=CartProduct.objects.all()
    for ep in r:
        print(ep.Pid)
        print(ep.Price)
        print(ep.quantity)
        s1=StatOrderDetails(StatOrderId=s,Pid=ep.Pid,Price=ep.Price,quantity=ep.quantity)
        s1.save()
        b=CartProduct.objects.all()
        b.delete()
    return render(request,'thanks1.html')
@login_required
def OrderShow1(request):
    context={}
    context['instance']=StatOrder.objects.all().order_by('-StatOrderId')
    if request.method=="POST":
        value=request.POST.get('StudentNumber')
        print(value)
        if StatOrder.objects.filter(UserId=value).exists():
            context['s1']=StatOrder.objects.filter(UserId=value).reverse()
            print(context['s1'])
            return OrderShowById1(request,context)
        else:
            messages.warning(request,"No order on this Enrolment number")
            return HttpResponseRedirect("/Stationary/OrderShow1/")
    return render(request,'OrderShow1.html',context)

@login_required
def OrderShowById1(request,context):
    return render(request,'OrderShowById1.html',context)
@login_required
def DetailOfOrderById1(request):
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
    return render(request,'DetailOfOrderById1.html',context)

@login_required
def putquery(request):
    context={}
    if request.method=="GET":
        form=QueryForm()
    elif request.method=="POST":
        print("hello rohit chaudhry")
        form=QueryForm(data=request.POST)
        if form.is_valid():
            pro=form.save()
            print("hello ronak patel")
            messages.success(request,"query is sent to the admin")
            return HttpResponseRedirect("/Stationary/Scategory_index/")
    context["form"]=form
    return render(request,"putquery.html",context)
