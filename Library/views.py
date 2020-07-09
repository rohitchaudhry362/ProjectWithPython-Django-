from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from Library.models import BookCategory,Stream,Book,BookCart,BookStock,LibraryOrder,BookCart,LibOrderDetails
from Library.forms import BookCategoryForm,StreamForm,StreamEditForm,AddBookForm,EditBookForm,BookStockForm,LibOrderForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'Library_home.html')

def BookCategoryIndex(request):
    context={}
    context['s']=BookCategory.objects.all()
    return render(request,'BookCategoryIndex.html',context)
def AddBookCategory(request):
    context = {}
    if request.method == 'GET':
        form = BookCategoryForm()
    elif request.method == "POST":
        form = BookCategoryForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            cat = form.save()

            return HttpResponseRedirect('/Library/BookCategoryIndex/')
    context['form'] = form
    return render(request, 'AddBookCategory.html', context)
def EditBookCategory(request):
    context = {}
    if request.method == 'GET' and 'BookCatId' in request.GET:
        BookCatId = request.GET['BookCatId']
        context['BookCatId'] = BookCatId
        instance = BookCategory.objects.get(BookCatId=BookCatId)
        form = BookCategoryForm(instance=instance)

    elif request.method == "POST":
        BookCatId = request.GET['BookCatId']
        instance = BookCategory.objects.get(BookCatId=BookCatId)
        form = BookCategoryForm(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"category %s is updated Sucessfully"%pro.BookCatName)
            return HttpResponseRedirect('/Library/BookCategoryIndex/')
    else:
        return HttpResponse("category id is mandaory")
    context['form'] = form
    return render(request, 'AddBookCategory.html', context)
def DeleteBookCategory(request):
    context = {}
    if request.method == 'GET' and 'BookCatId' in request.GET:
        BookCatId = request.GET['BookCatId']
        instance=BookCategory.objects.get(BookCatId=BookCatId)
        context['BookCatId'] = instance
    elif request.method == "POST":
        BookCatId = request.GET['BookCatId']
        instance = BookCategory.objects.get(BookCatId=BookCatId)
        messages.success(request, "Category <strong>%s</strong> is Deleted "%instance.BookCatName)
        instance.delete()
        return HttpResponseRedirect('/Library/BookCategoryIndex')
    else:
        return HttpResponse("category id is mandaory")

    return render(request, 'DeleteBookCategory.html', context)

def StreamForBookCat(request):
    context={ }

    BookCatId = request.GET['BookCatId']
    request.session['BookCatId']=BookCatId
    CatId1 = BookCategory.objects.get(BookCatId=BookCatId)
    Cpro1  = CatId1.stream_set.all()
    context={
        'CatId1':CatId1,
        'Cpro1':Cpro1,

    }
    return render(request,'StreamForBookCat.html',context)

def AddStream(request):
    context={}
    if request.method=="GET":
        form=StreamForm()
    elif request.method=="POST":
        form=StreamForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            pro=form.save()
            messages.success(request,"New Stream is added succesfully")
            Latest=Stream.objects.latest()
            got_cat_id=Latest.BookCatId_id
            return HttpResponseRedirect('/Library/StreamForBookCat/?BookCatId='+str(got_cat_id))
    context['form']=form
    return render(request, 'AddStream.html', context)
def EditStream(request):
    context = {}
    if request.method == 'GET' and 'StreamId' in request.GET:
        StreamId = request.GET['StreamId']
        context['StreamId'] = StreamId
        instance = Stream.objects.get(StreamId=StreamId)
        form = StreamEditForm(instance=instance)

    elif request.method == "POST":
        StreamId = request.GET['StreamId']
        instance = Stream.objects.get(StreamId=StreamId)
        temp=instance.BookCatId_id
        form = StreamEditForm(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"Stream '%s' is updated Sucessfully"%pro.StreamName)
            return HttpResponseRedirect('/Library/StreamForBookCat/?BookCatId='+str(temp))
    else:
        return HttpResponse("Product id is mandaory")
    context['form'] = form
    return render(request, 'AddStream.html', context)

def DeleteStream(request):
    context = {}
    if request.method == 'GET' and 'StreamId' in request.GET:
        StreamId = request.GET['StreamId']
        instance=Stream.objects.get(StreamId=StreamId)
        context['StreamId'] = instance
    elif request.method == "POST":
        StreamId = request.GET['StreamId']
        instance = Stream.objects.get(StreamId=StreamId)
        temp=instance.BookCatId_id
        messages.success(request, "Stream <strong>%s</strong> is Deleted "%instance.StreamName)
        instance.delete()
        return HttpResponseRedirect('/Library/StreamForBookCat/?BookCatId='+str(temp))
    else:
        return HttpResponse("product id is mandaory")

    return render(request, 'DeleteStream.html', context)

def AddBook(request):
    context={}
    if request.method=="GET":
        StreamId=request.GET['StreamId']
        BookCatId=request.session['BookCatId']
        BookCatIdName=BookCategory.objects.get(BookCatId=BookCatId)
        print(BookCatIdName)
        StreamIdName=Stream.objects.get(StreamId=StreamId)
        print(StreamIdName)
        template=loader.get_template('AddBook.html')
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
            Latest=Book.objects.latest()
            got_cat_id=Latest.BookCatId_id
            return HttpResponseRedirect('/Library/StreamForBookCat/?BookCatId='+str(got_cat_id))
    context['form']=form
    return HttpResponse(template.render(context,request))

def ShowBook(request):
    context={}
    StreamId=request.GET['StreamId']
    BooksForStream=Book.objects.filter(StreamId=StreamId)
    print(BooksForStream)
    context['BooksForStream']=BooksForStream
    return render(request,'ShowBook.html',context)

def EditBook(request):
    context = {}
    if request.method == 'GET' and 'BookId' in request.GET:
        BookId = request.GET['BookId']
        context['BookId'] = BookId
        instance = Book.objects.get(BookId=BookId)
        context['instance']=instance
        print(instance.BookName)
        form = EditBookForm(instance=instance)
    elif request.method == "POST":
        BookId = request.POST['BookId']
        instance = Book.objects.get(BookId=BookId)
        form = EditBookForm(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid:
            pro = form.save()
            messages.success(request,"Book %s is updated Sucessfully"%pro.BookName)
            temp=instance.StreamId_id
            return HttpResponseRedirect('/Library/ShowBook/?StreamId='+str(temp))
    else:
        return HttpResponse("Book id is mandaory")
    context['form'] = form
    return render(request, 'EditBook.html', context)

def DeleteBook(request):
    context = {}
    if request.method == 'GET' and 'BookId' in request.GET:
        BookId = request.GET['BookId']
        instance=Book.objects.get(BookId=BookId)
        context['BookId'] = instance
    elif request.method == "POST":
        BookId = request.GET['BookId']
        instance = Book.objects.get(BookId=BookId)
        temp=instance.StreamId_id
        messages.success(request, "Book <strong>%s</strong> is Deleted "%instance.BookName)
        instance.delete()
        return HttpResponseRedirect('/Library/ShowBook/?StreamId='+str(temp))
    else:
        return HttpResponse("Book id is mandaory")

    return render(request, 'DeleteBook.html', context)
def AddBookStock(request):
    context={}
    if request.method=="GET" and "BookId" in request.GET:
        BookId=request.GET["BookId"]
        context["BookId"]=BookId
        #instance = Book.objects.get(BookId=BookId)
        form = BookStockForm()
    elif request.method == "POST":
        BookId = request.POST['BookId']
        instance = Book.objects.get(BookId=BookId)
        form = BookStockForm(data=request.POST)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"Book stock is updated Sucessfully")
            temp=instance.StreamId_id
            return HttpResponseRedirect('/Library/ShowBook/?StreamId='+str(temp))
    else:
        return HttpResponse("Book id is mandaory")
    context['form'] = form
    return render(request, 'AddBookStock.html', context)
def ShowStock(request):
    context={}
    if request.method=="GET" and "BookId" in request.GET:
        BookId=request.GET["BookId"]
        Book1 = Book.objects.get(BookId=BookId)
        context['temp']=Book1.StreamId_id
        context['Book1']=Book1
        Book2 = BookStock.objects.filter(BookId=BookId)
        context['Book2']=Book2
        return render(request,'ShowStock.html',context)



def BookOrder(request):
    context={}
    context['book']=BookCategory.objects.all()
    return render(request,'BookOrder.html',context)

def BookOrderStream(request):
    context={}
    BookCatId=request.GET['BookCatId']
    context['Stream']=Stream.objects.filter(BookCatId=BookCatId)
    return render(request,'BookOrderStream.html',context)
def ShowBookForOrder(request):
    context={}
    StreamId=request.GET['StreamId']
    context['Books']=Book.objects.filter(StreamId=StreamId)
    return render(request,'ShowBookForOrder.html',context)

def ShowStockForOrder(request):
    context={}
    if request.method=="GET" and "BookId" in request.GET:
        BookId=request.GET["BookId"]
        Book1 = Book.objects.get(BookId=BookId)
        context['temp']=Book1.StreamId_id
        context['Book1']=Book1
        Book2 = BookStock.objects.filter(BookId=BookId)
        context['Book2']=Book2
        return render(request,'ShowStockForOrder.html',context)

def AddToCart(request):
    context={}
    BookStockId=request.GET['BookStockId']
    print(BookStockId)
    s0=BookStock.objects.get(BookStockId=BookStockId)
    s0.Issued=True
    s0.save()
    BookId=s0.BookId_id
    s=Book.objects.get(BookId=BookId)
    s4=BookStock.objects.get(BookStockId=BookStockId)
    print(s.BookId)
    print(s.BookName)
    print(s.BookAuthorName)
    print(s.BookSerialNumber)
    print(s4.BookStockSerial)
    print(s.Edition)
    s1=BookCart(BookId=s.BookId,BookName=s.BookName,BookAuthorName=s.BookAuthorName,BookSerialNumber=s.BookSerialNumber,BookStockSerial=s0.BookStockSerial,Edition=s.Edition)
    s1.save()
    #print("hello rht")
    #print(s1)
    messages.success(request,"Book is added successfully to cart")
    return HttpResponseRedirect("/Library/BookOrder/")
def BookCart1(request):
    context={}
    context['instance']=BookCart.objects.all()
    return render(request,"BookCart.html",context)
def ClearCart(request):
    instance=BookCart.objects.all()
    instance.delete()
    messages.success(request,"cart is empty now.You can add new Books")
    return HttpResponseRedirect('/Library/BookOrder/')
def DeleteFromCart(request):

    BookStockSerial = request.GET['BookStockSerial']
    s=BookStock.objects.get(BookStockSerial=BookStockSerial)
    s.Issued=False
    s.save()
    BookId=s.BookId_id
    instance = BookCart.objects.get(BookId=BookId)
    messages.success(request, "Book is deleted from cart")
    instance.delete()
    return HttpResponseRedirect('/Library/BookCart1/')

def PlaceOrder(request):
    context={}
    if request.method == "GET":
        template=loader.get_template('PlaceOrder2.html')
        form = LibOrderForm()
    elif request.method == "POST":
        form=LibOrderForm(data=request.POST)
        if form.is_valid:
            pro=form.save()
            messages.success(request,'entered id succesfully')

            #instance=CartProduct.objects.all()
            #context['instance']=CartProduct.objects.all()
            return DetailOfOrder(request)
    context['form'] = form
    return HttpResponse(template.render(context,request))



def DetailOfOrder(request):
    s=LibraryOrder.objects.latest('LibOrderId')
    print(s.LibOrderId)
    r=BookCart.objects.all()
    print(r)
    for ep in r:
        print("hello rht")
        print(ep.BookId)
        print(ep.BookName)
        print(ep.BookSerialNumber)
        print(ep.BookStockSerial)
        print("hello rht1")
        s1=LibOrderDetails(LibOrderId=s,BookId=ep.BookId,BookName=ep.BookName,BookSerialNumber=ep.BookSerialNumber,BookStockSerial=ep.BookStockSerial)
        s1.save()
        print("hello rht2")
    b=BookCart.objects.all()
    b.delete()
    return render(request,'thanks2.html')




def OrderShow3(request):
    context={}
    context['instance']=LibraryOrder.objects.all().order_by('-LibOrderId')
    if request.method=="POST":
        value=request.POST.get('StudentNumber')
        print(value)
        context['s1']=LibraryOrder.objects.filter(UserId=value).order_by('-LibOrderId')
        print(context['s1'])
        return OrderShowById3(request,context)
    return render(request,'OrderShow3.html',context)
def OrderShowById3(request,context):
    return render(request,'OrderShowById3.html',context)


def DetailOfOrderById3(request):
    context={ }
    LibOrderId = request.GET['LibOrderId']
    print(LibOrderId)
    data=LibOrderDetails.objects.filter(LibOrderId=LibOrderId)
    context['data']=data
    return render(request,'DetailOfOrderById3.html',context)
