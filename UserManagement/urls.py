from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

urlpatterns = [
url(r'^$',views.index_view),
#url(r'^login/', views.signup),




#url(r'^UserRole/', views.UserRole),
 ]
