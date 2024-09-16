from django.shortcuts import render
from . models import products
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def productses(request):
    featured_products= products.objects.order_by('priority')[:4]
    latest_products= products.objects.order_by('-priority')[:4]
    corner={'featured_products':featured_products,'latest_products':latest_products}
    return render(request,'index.html',corner)
@login_required(login_url='customer_login')
def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_lists= products.objects.order_by('priority')[:6]
    product_paginator=Paginator(product_lists,4)
    product_lists=product_paginator.get_page(page)
    context={'products':product_lists}
    print(context)
    return render(request,'product_list.html',context)
def detailed_product(request,pk):
    productpass=products.objects.get(pk=pk)
    contexts={'productpass':productpass}
    return render(request,'detailed_product.html',contexts)
