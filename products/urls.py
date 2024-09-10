
from django.urls import path
from . import views

urlpatterns = [

      path('', views.productses,name="products"),
      path('products/', views.product_list,name="productslist"),
      path('productdetail/<pk>', views.detailed_product,name="detailedproduct"),
]