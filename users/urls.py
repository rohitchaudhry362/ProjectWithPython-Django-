from django.conf.urls import url,include
from . import views

urlpatterns = [
url(r'^$',views.index_view),
#url(r'^role/', views.role),
url(r'^register/', views.register),
url(r'^signup/', views.registration1),
#url(r'^profile/', views.profile),
url(r'^login1/', views.login1),
url(r'^studentdetail/', views.studentdetail),

url(r'^mobilenumber/', views.mobilenumber),


#url(r'^role/', views.role),
]
