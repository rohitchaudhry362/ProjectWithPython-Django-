from django.conf.urls import url,include
from . import views
from django.urls import path
from Librarian.views import *

urlpatterns = [
url(r'^$',views.index1,name="index1"),
url(r'logout/',views.logout1),
path('BookCategoryIndex1/',BookCategoryIndex1),
path('AddBookCategory1/',AddBookCategory1),
path('EditBookCategory1/',EditBookCategory1),
path('DeleteBookCategory1/',DeleteBookCategory1),
path('StreamForBookCat1/',StreamForBookCat1),
path('AddStream1/',AddStream1),
path('EditStream1/',EditStream1),
path('DeleteStream1/',DeleteStream1),
path('AddBook1/',AddBook1),
path('ShowBook1/',ShowBook1),
path('EditBook1/',EditBook1),
path('DeleteBook1/',DeleteBook1),
path('AddBookStock1/',AddBookStock1),
path('ShowStock1/',ShowStock1),
path('BookOrder1/',BookOrder1),
path('BookOrderStream1/',BookOrderStream1),
path('ShowBookForOrder1/',ShowBookForOrder1),
path('ShowStockForOrder1/',ShowStockForOrder1),
path('AddToCart1/',AddToCart1),
path('BookCart1/',BookCart2),
path('DeleteFromCart1/',DeleteFromCart1),
path('PlaceOrder3/',PlaceOrder3),
path('DetailOfOrder1/',DetailOfOrder1),
path('OrderShow4/',OrderShow4),
path('OrderShowById3/',OrderShowById3),
path('DetailOfOrderById3/',DetailOfOrderById3),
path('ReturnBook1/',ReturnBook1),
path('FineAmount/',FineAmount),
path('query/',putquery),
]
