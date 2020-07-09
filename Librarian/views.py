from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from Librarian.models import BookCategory1,Stream1,Book1,BookStock1,BookCart1,LibraryOrder1,LibOrderDetails1,ReturnBook,FineAmount1
from Librarian.forms import BookCategoryForm,StreamForm,StreamEditForm,AddBookForm,EditBookForm,BookStockForm,LibOrderForm,ReturnForm,FineAmountForm,QueryForm
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from users.views import MyUser
from django.contrib.auth import logout
from users.views import login1
from users.models import card,Student

@login_required
def logout1(request):
    logout(request)
    return login1(request)



@login_required
def index1(request):
    context={}
    username = request.session['username']
    context['username']=username
    s=MyUser.objects.get(user=username)
    context['data']=s
    return render(request,'Library_home1.html',context)
@login_required
def BookCategoryIndex1(request):
    context={}
    context['s']=BookCategory1.objects.all()
    return render(request,'BookCategoryIndex1.html',context)

@login_required
def AddBookCategory1(request):
    context = {}
    if request.method == 'GET':
        form = BookCategoryForm()
    elif request.method == "POST":
        form = BookCategoryForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            cat = form.save()
            return HttpResponseRedirect('/Librarian/BookCategoryIndex1/')
    context['form'] = form
    return render(request, 'AddBookCategory1.html', context)

@login_required
def EditBookCategory1(request):
    context = {}
    if request.method == 'GET' and 'BookCatId' in request.GET:
        BookCatId = request.GET['BookCatId']
        context['BookCatId'] = BookCatId
        instance = BookCategory1.objects.get(BookCatId=BookCatId)
        form = BookCategoryForm(instance=instance)

    elif request.method == "POST":
        BookCatId = request.GET['BookCatId']
        instance = BookCategory1.objects.get(BookCatId=BookCatId)
        form = BookCategoryForm(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"category %s is updated Sucessfully"%pro.BookCatName)
            return HttpResponseRedirect('/Librarian/BookCategoryIndex1/')
    else:
        return HttpResponse("category id is mandaory")
    context['form'] = form
    return render(request, 'AddBookCategory1.html', context)
@login_required
def DeleteBookCategory1(request):
    context = {}
    if request.method == 'GET' and 'BookCatId' in request.GET:
        BookCatId = request.GET['BookCatId']
        instance=BookCategory1.objects.get(BookCatId=BookCatId)
        context['BookCatId'] = instance
    elif request.method == "POST":
        BookCatId = request.GET['BookCatId']
        instance = BookCategory1.objects.get(BookCatId=BookCatId)
        messages.success(request, "Category <strong>%s</strong> is Deleted "%instance.BookCatName)
        instance.delete()
        return HttpResponseRedirect('/Librarian/BookCategoryIndex1')
    else:
        return HttpResponse("category id is mandaory")

    return render(request, 'DeleteBookCategory1.html', context)

@login_required
def StreamForBookCat1(request):
    context={ }

    BookCatId = request.GET['BookCatId']
    request.session['BookCatId']=BookCatId
    CatId1 = BookCategory1.objects.get(BookCatId=BookCatId)
    Cpro1  = CatId1.stream1_set.all()
    context={
        'CatId1':CatId1,
        'Cpro1':Cpro1,

    }
    return render(request,'StreamForBookCat1.html',context)

@login_required
def AddStream1(request):
    context={}
    if request.method=="GET":
        form=StreamForm()
    elif request.method=="POST":
        form=StreamForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            pro=form.save()
            messages.success(request,"New Stream is added succesfully")
            Latest=Stream1.objects.latest()
            got_cat_id=Latest.BookCatId_id
            return HttpResponseRedirect('/Librarian/StreamForBookCat1/?BookCatId='+str(got_cat_id))
    context['form']=form
    return render(request, 'AddStream1.html', context)
@login_required
def EditStream1(request):
    context = {}
    if request.method == 'GET' and 'StreamId' in request.GET:
        StreamId = request.GET['StreamId']
        context['StreamId'] = StreamId
        instance = Stream1.objects.get(StreamId=StreamId)
        form = StreamEditForm(instance=instance)

    elif request.method == "POST":
        StreamId = request.GET['StreamId']
        instance = Stream1.objects.get(StreamId=StreamId)
        temp=instance.BookCatId_id
        form = StreamEditForm(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"Stream '%s' is updated Sucessfully"%pro.StreamName)
            return HttpResponseRedirect('/Librarian/StreamForBookCat1/?BookCatId='+str(temp))
    else:
        return HttpResponse("Product id is mandaory")
    context['form'] = form
    return render(request, 'AddStream1.html', context)
@login_required
def DeleteStream1(request):
    context = {}
    if request.method == 'GET' and 'StreamId' in request.GET:
        StreamId = request.GET['StreamId']
        instance=Stream1.objects.get(StreamId=StreamId)
        context['StreamId'] = instance
    elif request.method == "POST":
        StreamId = request.GET['StreamId']
        instance = Stream1.objects.get(StreamId=StreamId)
        temp=instance.BookCatId_id
        messages.success(request, "Stream <strong>%s</strong> is Deleted "%instance.StreamName)
        instance.delete()
        return HttpResponseRedirect('/Librarian/StreamForBookCat1/?BookCatId='+str(temp))
    else:
        return HttpResponse("product id is mandaory")

    return render(request, 'DeleteStream1.html', context)
@login_required
def AddBook1(request):
    context={}
    if request.method=="GET":
        StreamId=request.GET['StreamId']
        BookCatId=request.session['BookCatId']
        BookCatIdName=BookCategory1.objects.get(BookCatId=BookCatId)
        print(BookCatIdName)
        StreamIdName=Stream1.objects.get(StreamId=StreamId)
        print(StreamIdName)
        template=loader.get_template('AddBook1.html')
        context={
        'StreamIdName':StreamId,
        'BookCatIdName':BookCatId,

        }

        form=AddBookForm()

    elif request.method=="POST":
        print("hello rht")
        form = AddBookForm(data=request.POST,files=request.FILES)
        if form.is_valid:
            pro=form.save()
            messages.success(request,"New Book is added succesfully")
            Latest=Book1.objects.latest()
            got_cat_id=Latest.BookCatId_id
            return HttpResponseRedirect('/Librarian/StreamForBookCat1/?BookCatId='+str(got_cat_id))
    context['form']=form
    return HttpResponse(template.render(context,request))
@login_required
def ShowBook1(request):
    context={}
    StreamId=request.GET['StreamId']
    BooksForStream=Book1.objects.filter(StreamId=StreamId)
    print(BooksForStream)
    context['BooksForStream']=BooksForStream
    return render(request,'ShowBook1.html',context)

@login_required
def EditBook1(request):
    context = {}
    if request.method == 'GET' and 'BookId' in request.GET:
        BookId = request.GET['BookId']
        context['BookId'] = BookId
        instance = Book1.objects.get(BookId=BookId)
        context['instance']=instance
        print(instance.BookName)
        form = EditBookForm(instance=instance)
    elif request.method == "POST":
        BookId = request.POST['BookId']
        instance = Book1.objects.get(BookId=BookId)
        form = EditBookForm(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid:
            pro = form.save()
            messages.success(request,"Book %s is updated Sucessfully"%pro.BookName)
            temp=instance.StreamId_id
            return HttpResponseRedirect('/Librarian/ShowBook1/?StreamId='+str(temp))
    else:
        return HttpResponse("Book id is mandaory")
    context['form'] = form
    return render(request, 'EditBook1.html', context)

@login_required
def DeleteBook1(request):
    context = {}
    if request.method == 'GET' and 'BookId' in request.GET:
        BookId = request.GET['BookId']
        instance=Book1.objects.get(BookId=BookId)
        context['BookId'] = instance
    elif request.method == "POST":
        BookId = request.GET['BookId']
        instance = Book1.objects.get(BookId=BookId)
        temp=instance.StreamId_id
        messages.success(request, "Book <strong>%s</strong> is Deleted "%instance.BookName)
        instance.delete()
        return HttpResponseRedirect('/Librarian/ShowBook1/?StreamId='+str(temp))
    else:
        return HttpResponse("Book id is mandaory")

    return render(request, 'DeleteBook1.html', context)
@login_required
def AddBookStock1(request):
    context={}
    if request.method=="GET" and "BookId" in request.GET:
        BookId=request.GET["BookId"]
        context["BookId"]=BookId
        #instance = Book.objects.get(BookId=BookId)
        form = BookStockForm()
    elif request.method == "POST":
        BookId = request.POST['BookId']
        instance = Book1.objects.get(BookId=BookId)
        form = BookStockForm(data=request.POST)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"Book stock is updated Sucessfully")
            temp=instance.StreamId_id
            return HttpResponseRedirect('/Librarian/ShowBook1/?StreamId='+str(temp))
    else:
        return HttpResponse("Book id is mandaory")
    context['form'] = form
    return render(request, 'AddBookStock1.html', context)
@login_required
def ShowStock1(request):
    context={}
    if request.method=="GET" and "BookId" in request.GET:
        BookId=request.GET["BookId"]
        Book3 = Book1.objects.get(BookId=BookId)
        context['temp']=Book3.StreamId_id
        context['Book1']=Book3
        Book2 = BookStock1.objects.filter(BookId=BookId)
        context['Book2']=Book2
        return render(request,'ShowStock1.html',context)

@login_required
def BookOrder1(request):
    context={}
    context['book']=BookCategory1.objects.all()
    return render(request,'BookOrder1.html',context)
@login_required
def BookOrderStream1(request):
    context={}
    BookCatId=request.GET['BookCatId']
    context['Stream']=Stream1.objects.filter(BookCatId=BookCatId)
    return render(request,'BookOrderStream1.html',context)
@login_required
def ShowBookForOrder1(request):
    context={}
    StreamId=request.GET['StreamId']
    context['Books']=Book1.objects.filter(StreamId=StreamId)
    return render(request,'ShowBookForOrder1.html',context)
@login_required
def ShowStockForOrder1(request):
    context={}
    if request.method=="GET" and "BookId" in request.GET:
        BookId=request.GET["BookId"]
        Book3 = Book1.objects.get(BookId=BookId)
        context['temp']=Book3.StreamId_id
        context['Book1']=Book3
        Book2 = BookStock1.objects.filter(BookId=BookId)
        context['Book2']=Book2
        return render(request,'ShowStockForOrder1.html',context)
@login_required
def AddToCart1(request):
    context={}
    BookStockId=request.GET['BookStockId']
    print(BookStockId)
    s0=BookStock1.objects.get(BookStockId=BookStockId)
    s0.Issued=True
    s0.save()
    BookId=s0.BookId_id
    s=Book1.objects.get(BookId=BookId)
    s4=BookStock1.objects.get(BookStockId=BookStockId)
    print(s.BookId)
    print(s.BookName)
    print(s.BookAuthorName)
    print(s.BookSerialNumber)
    print(s4.BookStockSerial)
    print(s.Edition)
    s1=BookCart1(BookId=s.BookId,BookName=s.BookName,BookAuthorName=s.BookAuthorName,BookSerialNumber=s.BookSerialNumber,BookStockSerial=s0.BookStockSerial,Edition=s.Edition)
    s1.save()
    #print("hello rht")
    #print(s1)
    messages.success(request,"Book is added successfully to cart")
    return HttpResponseRedirect("/Librarian/BookOrder1/")
@login_required
def BookCart2(request):
    context={}
    context['instance']=BookCart1.objects.all()
    return render(request,"BookCart1.html",context)



@login_required
def DeleteFromCart1(request):

    BookStockSerial = request.GET['BookStockSerial']
    s=BookStock1.objects.get(BookStockSerial=BookStockSerial)
    s.Issued=False
    s.save()
    BookId=s.BookId_id
    instance = BookCart1.objects.get(BookId=BookId)
    messages.success(request, "Book is deleted from cart")
    instance.delete()
    return HttpResponseRedirect('/Librarian/BookCart1/')

@login_required
def PlaceOrder3(request):
    context={}
    if request.method == "GET":
        template=loader.get_template('PlaceOrder3.html')
        form = LibOrderForm()
    elif request.method == "POST":
        form=LibOrderForm(data=request.POST)
        if form.is_valid:
            pro=form.save()
            UserId = form.cleaned_data.get('UserId')
            print("hello buddy")
            print(UserId)
            if Student.objects.filter(enroll=UserId).exists():
                messages.success(request,'entered id succesfully')
                return DetailOfOrder1(request)
            else:
                s=LibraryOrder1.objects.latest()
                print(s)
                print(s.LibOrderId)
                s.delete()
                books=BookCart1.objects.all()
                print(books)
                for x in books:
                    print(x.BookSerialNumber)
                for x in books:
                    y=BookStock1.objects.get(BookStockSerial=x.BookStockSerial)
                    print("in the loop")
                    print(y.BookStockSerial)
                    print(y.Issued)
                    y.Issued=False
                    y.save()
                books.delete()
                messages.warning(request,"the enrollment is not registered")
                return HttpResponseRedirect('/Librarian/PlaceOrder3/')

    context['form'] = form
    return HttpResponse(template.render(context,request))
@login_required
def DetailOfOrder1(request):
    s=LibraryOrder1.objects.latest('LibOrderId')
    print(s.LibOrderId)
    r=BookCart1.objects.all()
    print(r)
    for ep in r:
        print("hello rht")
        print(ep.BookId)
        print(ep.BookName)
        print(ep.BookSerialNumber)
        print(ep.BookStockSerial)
        print("hello rht1")
        s1=LibOrderDetails1(LibOrderId=s,BookId=ep.BookId,BookName=ep.BookName,BookSerialNumber=ep.BookSerialNumber,BookStockSerial=ep.BookStockSerial)
        s1.save()
        print("hello rht2")
    b=BookCart1.objects.all()
    b.delete()
    return render(request,'thanks3.html')
@login_required
def OrderShow4(request):
    context={}
    context['instance']=LibraryOrder1.objects.all().order_by('-LibOrderId')
    if request.method=="POST":
        value=request.POST.get('StudentNumber')
        print(value)
        if LibraryOrder1.objects.filter(UserId=value):
            context['s1']=LibraryOrder1.objects.filter(UserId=value).order_by('-LibOrderId')
            print(context['s1'])
            return OrderShowById3(request,context)
        else:
            messages.warning(request,"No orders on this enrolment")
            return HttpResponseRedirect("/Librarian/OrderShow4/")
    return render(request,'OrderShow4.html',context)
@login_required
def OrderShowById3(request,context):
    return render(request,'OrderShowById4.html',context)
@login_required
def DetailOfOrderById3(request):
    context={ }
    LibOrderId = request.GET['LibOrderId']
    print(LibOrderId)
    data=LibOrderDetails1.objects.filter(LibOrderId=LibOrderId)
    context['data']=data
    return render(request,'DetailOfOrderById4.html',context)
@login_required
def ReturnBook1(request):
    context={ }
    if request.method=="GET":
        BookStockSerial=request.GET['BookStockSerial']
        context["BookStockSerial"]=BookStockSerial
        s=LibOrderDetails1.objects.get(BookStockSerial=BookStockSerial)
        id=s.LibOrderId_id
        print(id)
        s=LibraryOrder1.objects.get(LibOrderId=id)
        print(s.DateOfOrder)
        context['dateoforder']=s.DateOfOrder

        form=ReturnForm()
    elif request.method == "POST":
        form=ReturnForm(data=request.POST)
        if form.is_valid:
            pro=form.save()
            #messages.success(request,'form submitted successfully')
            latest=ReturnBook.objects.latest()
            s=latest.ReturnId
            return HttpResponseRedirect("/Librarian/FineAmount/?ReturnId="+str(s))
    context['form'] = form
    return render(request, 'ReturnBook1.html', context)

@login_required
def FineAmount(request):
    context={}
    if request.method=="GET":
        ReturnId=request.GET['ReturnId']
        s=ReturnBook.objects.get(ReturnId=ReturnId)
        print("hello rht")
        print(s.DateOfOrder)
        print(s.ReturnDate)
        date_format = "%Y-%m-%d"
        a = datetime.strptime(str(s.DateOfOrder), date_format)
        b = datetime.strptime(str(s.ReturnDate), date_format)
        delta = b - a
        print(delta.days)
        if delta.days>7:
            fine=(delta.days-7)*50
        else:
            fine=0
            context['fine']=fine
        form=FineAmountForm()
    elif request.method=="POST":
        ReturnId=request.GET['ReturnId']
        s=ReturnBook.objects.get(ReturnId=ReturnId)
        form=FineAmountForm(data=request.POST)
        if form.is_valid:
            pro=form.save()
            s1=BookStock1.objects.get(BookStockSerial=s.BookStockSerial)
            s1.Issued=False
            s1.save()
            s2=LibOrderDetails1.objects.get(BookStockSerial=s.BookStockSerial)
            s2.IsReturned=True
            s2.save()

            messages.success(request,"Book Returned successfully")
            return HttpResponseRedirect("/Librarian/OrderShow4/")
    context['form']=form
    return render(request, 'FineAmount.html', context)


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
            return HttpResponseRedirect("/Librarian/BookCategoryIndex1/")
    context["form"]=form
    return render(request,"putquery1.html",context)
