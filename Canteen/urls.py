from django.conf.urls import url,include
from . import views
from django.urls import path
from Canteen.views import *

urlpatterns = [
url(r'^$',views.index,name="index"),
url(r'^logout/$',views.logout1),
path('Ccategory_index/',Ccategory_index),
path('add_Ccategory/', create_Ccategory),
path('edit_Ccategory/',edit_Ccategory),
path('delete_Ccategory/',delete_Ccategory),

path('Cproduct_index/',Cproduct_index),
path('add_Cproduct/', create_Cproduct),
path('edit_Cproduct/',edit_Cproduct),
path('delete_Cproduct/',delete_Cproduct),
path('CproductbyId/',CproductbyId),
path('Ccategory_order/',Ccategory_order),
path('Ccategory_order_productbyId/',Ccategory_order_productbyid),
#path('Ccategory_order_productbyId/Corder_details/',OrderDetails),
path('Ccategory_order_productbyId/productdetail/',productdetail),
path('CanteenCart/',CartShow),
path('ClearCart/',ClearCart),
path("EditFromCart/",EditFromCart),
path('DeleteFromCart/',DeleteFromCart),
path('PlaceOrder/',PlaceOrder),
path('OrderShow/',OrderShow),
path('OrderShowById/',OrderShowById),
path('DetailOfOrder/',DetailOfOrder),
path('DetailOfOrderById/',DetailOfOrderById),
path('barcode/',Barcode),
path('query/',putquery),
path('sendsms/',sendsms),
]
