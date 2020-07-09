from django.conf.urls import url,include
from . import views
from django.urls import path
from Library.views import *

urlpatterns = [
url(r'^$',views.index,name="index"),
path('BookCategoryIndex/',BookCategoryIndex),
path('AddBookCategory/',AddBookCategory),
path('EditBookCategory/',EditBookCategory),
path('DeleteBookCategory/',DeleteBookCategory),
path('StreamForBookCat/',StreamForBookCat),
path('AddStream/',AddStream),
path('EditStream/',EditStream),
path('DeleteStream/',DeleteStream),
path('AddBook/',AddBook),
path('ShowBook/',ShowBook),
path('EditBook/',EditBook),
path('BookOrder/',BookOrder),
path('BookOrderStream/',BookOrderStream),
path('DeleteBook/',DeleteBook),
path('EditBook/',EditBook),
path('ShowBookForOrder/',ShowBookForOrder),
path('AddToCart/',AddToCart),
path('ClearCart/',ClearCart),
path('BookCart1/',BookCart1),
path('AddBookStock/',AddBookStock),
path('ShowStock/',ShowStock),
path('ShowStockForOrder/',ShowStockForOrder),
path('DeleteFromCart/',DeleteFromCart),
path('PlaceOrder/',PlaceOrder),
path('DetailOfOrder/',DetailOfOrder),
path('OrderShow3/',OrderShow3),
path('OrderShowById3/',OrderShowById3),
path('DetailsForOrderById3/',DetailOfOrderById3),
path('DeleteBook/',DeleteBook),

]
