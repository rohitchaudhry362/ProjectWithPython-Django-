from django.conf.urls import url,include
from . import views
from django.urls import path
from Student.views import *


urlpatterns = [
path('index_view/',index),
url(r'^logout/$',views.logout1),
path('OrderShowForC/',OrderShowForC),
path('uploaddoc/',uploaddoc),
path('updatedoc/',updatedoc),
path('DetailOfOrderForC/',DetailOfOrderForC),
path('OrderShowForS/',OrderShowForS),
path('DetailOfOrderForS/',DetailOfOrderForS),
path('OrderShowForL/',OrderShowForL),
path('DetailOfOrderForL/',DetailOfOrderForL),
path('updateprofile/',updateprofile),
path('updatesem/',updatesem),
path('blockcard/',blockcard),
]
