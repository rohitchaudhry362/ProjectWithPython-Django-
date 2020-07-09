from django.conf.urls import url,include
from . import views
from django.urls import path
from myadmin.views import *

urlpatterns = [
url(r'^$',views.index,name="index"),
path('studentlist/',studentlist),
path('studentprofile/',studentprofile),
path('updatebalance/',updatebalance),
path('showdocs/',showdocs),
path('respondqueries/',respondqueries),
path('reviewqueries/',reviewqueries),

]
