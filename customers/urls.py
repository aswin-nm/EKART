
from django.urls import path
from . import views

urlpatterns = [

     
      path('customer_login/', views.customer_login,name="customer_login"),
     
]