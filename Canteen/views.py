from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from Canteen.models import Ccategory, Cproduct,CartProduct,CatOrder,CatOrderDetails
from users.views import login1
from users.models import MyUser,card,Query,Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Canteen.forms import CcategoryForm,CproductForm,CcategoryDelete,CproductDelete,CproductEdit,CartProductForm,CatOrderForm,EditCartProduct,QueryForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
import barcode,pyqrcode,requests
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
    return render(request,'Ccategory_home.html',context)
@login_required
def Ccategory_index(request):
    context={}
    context['cat']=Ccategory.objects.all()
    return render(request,'Ccategory_index.html',context)
@login_required
def create_Ccategory(request):
    context = {}
    if request.method == 'GET':
        form = CcategoryForm()
    elif request.method == "POST":
        form = CcategoryForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            cat = form.save()

            return HttpResponseRedirect('/Canteen/Ccategory_index/')
    context['form'] = form
    return render(request, 'Ccategory_create.html', context)
@login_required
def edit_Ccategory(request):
    context = {}
    if request.method == 'GET' and 'CatId' in request.GET:
        CatId = request.GET['CatId']
        context['CatId'] = CatId
        instance = Ccategory.objects.get(CatId=CatId)
        print("hgello rht",instance)
        form = CcategoryForm(instance=instance)

    elif request.method == "POST":
        CatId = request.POST['CatId']
        instance = Ccategory.objects.get(CatId=CatId)
        form = CcategoryForm(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"category %s is updated Sucessfully" %pro.CatName)
            return HttpResponseRedirect('/Canteen/Ccategory_index/')
    else:
        return HttpResponse("category id is mandaory")
    context['form'] = form
    return render(request, 'Ccategory_create.html', context)
@login_required
def delete_Ccategory(request):
    context = {}
    if request.method == 'GET' and 'CatId' in request.GET:
        CatId = request.GET['CatId']
        instance=Ccategory.objects.get(CatId=CatId)
        context['CatId'] = instance
    elif request.method == "POST":
        CatId = request.GET['CatId']
        instance = Ccategory.objects.get(CatId=CatId)
        messages.success(request, "Category <strong>%s</strong> is Deleted "%instance.CatName)
        instance.delete()
        return HttpResponseRedirect('/Canteen/Ccategory_index')
    else:
        return HttpResponse("category id is mandaory")

    return render(request, 'Ccategory_delete.html', context)
@login_required
def Ccategory_order(request):
    context={}
    context['cat']=Ccategory.objects.all()
    return render(request,'Ccategory_order.html',context)
@login_required
def Cproduct_index(request):
    context={}
    context['pro']=Cproduct.objects.all()
    return render(request,"Cproduct_index.html",context)
@login_required
def edit_Cproduct(request):
    context = {}
    if request.method == 'GET' and 'Pid' in request.GET:
        Pid = request.GET['Pid']
        context['Pid'] = Pid
        instance = Cproduct.objects.get(Pid=Pid)
        form = CproductEdit(instance=instance)

    elif request.method == "POST":
        Pid = request.POST['Pid']
        instance = Cproduct.objects.get(Pid=Pid)
        temp=instance.CatId_id
        form = CproductEdit(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"Product '%s' is updated Sucessfully"%pro.PName)
            return HttpResponseRedirect('/Canteen/CproductbyId/?CatId='+str(temp))
    else:
        return HttpResponse("Product id is mandaory")
    context['form'] = form
    return render(request, 'Cproduct_create.html', context)
@login_required
def create_Cproduct(request):
    context = {}
    if request.method == 'GET':
        form = CproductForm()
    elif request.method == "POST":
        form = CproductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,'new product is added successfully')
            Latest=Cproduct.objects.latest()
            got_cat_id=Latest.CatId_id
            return HttpResponseRedirect('/Canteen/CproductbyId/?CatId='+str(got_cat_id))
    context['form']=form
    return render(request, 'Cproduct_create.html', context)
@login_required
def delete_Cproduct(request):
    context = {}
    if request.method == 'GET' and 'Pid' in request.GET:
        Pid = request.GET['Pid']
        instance=Cproduct.objects.get(Pid=Pid)
        context['Pid'] = instance
    elif request.method == "POST":
        Pid = request.GET['Pid']
        instance = Cproduct.objects.get(Pid=Pid)
        temp=instance.CatId_id
        messages.success(request, "product <strong>%s</strong> is Deleted "%instance.PName)
        instance.delete()
        return HttpResponseRedirect('/Canteen/CproductbyId/?CatId='+str(temp))
    else:
        return HttpResponse("product id is mandaory")

    return render(request, 'Cproduct_delete.html', context)
@login_required
def CproductbyId(request):
    context={ }
    CatId = request.GET['CatId']
    CatId1 = Ccategory.objects.get(CatId=CatId)
    Cpro1  = CatId1.cproduct_set.all()
    context={
        'CatId1':CatId1,
        'Cpro1':Cpro1,

    }
    return render(request,'CproductbyId.html',context)
@login_required
def Ccategory_order_productbyid(request):
    context={ }
    CatId = request.GET['CatId']
    CatId1 = Ccategory.objects.get(CatId=CatId)
    Cpro1  = CatId1.cproduct_set.all()
    context={
        'CatId1':CatId1,
        'Cpro1':Cpro1,

    }
    return render(request,'Ccategory_order_productbyid.html',context)
@login_required
def OrderDetails(request):
    context={ }
    Pid = request.GET['Pid']
    Pid1 = Cproduct.objects.get(Pid=Pid)
    #Cpro1  = CatId1.cproduct_set.all()
    context={

        'Pid1':Pid1,

    }
    return render(request,'Corder_details.html',context)
@login_required
def productdetail(request):
    context={}
    if request.method == "GET":
        Pid = request.GET['Pid']
        pro=Cproduct.objects.filter(Pid=Pid)

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
                messages.success(request,"product is already added in the cart.You can add/remove quantity from cart")
                s=CartProduct.objects.latest()
                s.delete()
                return HttpResponseRedirect('/Canteen/CanteenCart/')
            else:
                messages.success(request,' product is added successfully to cart')
                return HttpResponseRedirect('/Canteen/Ccategory_order/')
    context['form'] = form
    return render(request,"productdetail.html",context)
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
    return render(request,'CanteenCart.html',context)
@login_required
def ClearCart(request):
    instance=CartProduct.objects.all()
    instance.delete()
    messages.success(request,"cart is empty now.You can add new products")
    return HttpResponseRedirect('/Canteen/Ccategory_order')
@login_required
def EditFromCart(request):
    context={}
    if request.method=='GET' and 'Pid' in request.GET:
        Pid = request.GET['Pid']
        context['Pid']=Pid
        instance=CartProduct.objects.get(Pid=Pid)
        form=EditCartProduct(instance=instance)
    elif request.method=="POST":
        Pid=request.POST['Pid']
        instance=CartProduct.objects.get(Pid=Pid)
        form=EditCartProduct(data=request.POST,instance=instance)
        if form.is_valid():
            pro=form.save()
            messages.success(request,"cart updated successfully")
            return HttpResponseRedirect("/Canteen/CanteenCart/")
    else:
        return HttpResponse("product id is mandatory")
    context["form"]=form
    return render(request,"EditFromCart.html",context)


@login_required
def DeleteFromCart(request):
    Pid = request.GET['Pid']
    instance = CartProduct.objects.get(Pid=Pid)
    messages.success(request, "product is deleted from cart")
    instance.delete()
    return HttpResponseRedirect('/Canteen/CanteenCart/')
def PlaceOrder(request):
    context={}
    if request.method == "GET":
        #Pid = request.GET['Pid']
        #pro=Cproduct.objects.filter(Pid=Pid)
        #set_views_count("product", request, pro[0])
        template=loader.get_template('PlaceOrder.html')
        form = CatOrderForm()
    elif request.method == "POST":
        form=CatOrderForm(data=request.POST)

        if form.is_valid():
            form.save()
            print("this is line 1")
            UserId=form.cleaned_data.get('UserId')


            if card.objects.filter(enroll=UserId).exists():
                s=card.objects.get(enroll=UserId)
                if(s.isblocked==True):
                    instance=CatOrder.objects.latest()
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
                        return DetailOfOrder(request)
                    else:
                        instance=CatOrder.objects.latest()
                        instance.delete()
                        messages.warning(request,"not sufficient amount in the card")
                        return CartShow(request)
            else:
                instance=CatOrder.objects.latest()
                instance.delete()
                messages.warning(request,"the userid is not registered")
                return CartShow(request)
    context['form'] = form
    return HttpResponse(template.render(context,request))
@login_required
def OrderShow(request):
    context={}
    context['instance']=CatOrder.objects.all().order_by('-CatOrderId')
    if request.method=="POST":
        value=request.POST.get('StudentNumber')
        print(value)
        if CatOrder.objects.filter(UserId=value).exists():
            context['s1']=CatOrder.objects.filter(UserId=value).order_by('-CatOrderId')
            print(context['s1'])
            return OrderShowById(request,context)
        else:
            messages.warning(request,"No order on this Enrolment number")
            return HttpResponseRedirect("/Canteen/OrderShow/")

    return render(request,'OrderShow.html',context)
@login_required
def OrderShowById(request,context):
    return render(request,'OrderShowById.html',context)
@login_required
def DetailOfOrder(request):
    s=CatOrder.objects.latest('CatOrderId')
    print(s.CatOrderId)
    r=CartProduct.objects.all()
    for ep in r:
        print(ep.Pid)
        print(ep.Price)
        print(ep.quantity)
        s1=CatOrderDetails(CatOrderId=s,Pid=ep.Pid,Price=ep.Price,quantity=ep.quantity)
        s1.save()
        b=CartProduct.objects.all()
        b.delete()
    return render(request,'thanks.html')
@login_required
def DetailOfOrderById(request):
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
    return render(request,'DetailOfOrderById.html',context)

def Barcode(request):
        num=151260107051
        image=barcode.get_barcode_class('ean13')
        image_bar=image(u'{}'.format(num))
        file=open('F:\\rhtbarcode.svg','wb')
        image_bar.write(file)
        return HttpResponse("barcoede genereatfeytg")
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
            return HttpResponseRedirect("/Canteen/Ccategory_index/")
    context["form"]=form
    return render(request,"putquery.html",context)


def sendsms(request):
    url = "https://smsapi.engineeringtgr.com/send/"
    params = dict(
        Mobile='8264327271',
        Password='Iamrht362@',
        Key='rohity1TUrdf6wi2LA35FYo07m',
        Message='hello',
        To='9998860958')

    resp = requests.get(url, params)
    print(resp, resp.text)
