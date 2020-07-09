from django.conf.urls import url,include
from . import views
from django.urls import path
from Stationary.views import *

urlpatterns = [
url(r'^$',views.index,name="index"),
url(r'logout',views.logout1),
path('Scategory_index/',Scategory_index),
path('add_Scategory/', create_Scategory),
path('edit_Scategory/',edit_Scategory),
path('delete_Scategory/',delete_Scategory),

path('Sproduct_index/',Sproduct_index),
path('add_Sproduct/', create_Sproduct),
path('edit_Sproduct/',edit_Sproduct),
path('delete_Sproduct/',delete_Sproduct),
path('SproductbyId/',SproductbyId),
path('Scategory_order/',Scategory_order),
path('Scategory_order_productbyId/',Scategory_order_productbyid),
path('Scategory_order_productbyId/productdetail/',productdetail),
path('StationaryCart/',CartShow),
path('ClearCart/',ClearCart),
path('EditFromCart1/',EditFromCart),
path('DeleteFromCart1/',DeleteFromCart),
path('PlaceOrder1/',PlaceOrder),
path('DetailOfOrder1/',DetailOfOrder1),
path('OrderShow1/',OrderShow1),
path('OrderShowById1/',OrderShowById1),
path('DetailOfOrderById1/',DetailOfOrderById1),
path('query/',putquery),



]
