from django.shortcuts import render,redirect,get_object_or_404
from . models import order,orderditem
from products.models import products
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customers.models import customer as Customer

# Create your views here.
@login_required(login_url='customer_login')
def cart(request):
    
        
        user=request.user
        customer, _ = Customer.objects.get_or_create(user=user, defaults={'name': user.username, 'address': 'Not provided'})
       
        cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )
        context={'cart':cart_obj}

        return render(request,'cart.html',context)

@login_required(login_url='customer_login')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer, _ = Customer.objects.get_or_create(user=user, defaults={'name': user.username, 'address': 'Not provided'})
        quantity=int(request.POST.get('quantity',0))
        product_id=request.POST.get('product_id')
        cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )
        product=products.objects.get(pk=product_id)
        ordered_item,created=orderditem.objects.get_or_create(
             product=product,
             owner=cart_obj,
        )
        if created:
             ordered_item.quantity=quantity
             ordered_item.save()
        else:
             ordered_item.quantity=ordered_item.quantity+quantity 
             ordered_item.save()    
        return redirect('cart')
    
@login_required(login_url='customer_login')
def delete_item(request,pk):
     item=orderditem.objects.get(pk=pk)
     if item:
          item.delete()   
     return redirect('cart')    

@login_required(login_url='customer_login')
def checkout(request):
     if request.POST:
          try:
               user=request.user
               customer, _ = Customer.objects.get_or_create(user=user, defaults={'name': user.username, 'address': 'Not provided'})
               total=float(request.POST.get('total'))
               order_obj=order.objects.get(
                    owner=customer,
                    order_status=order.CART_STAGE
                      )
               if order_obj:
                    order_obj.order_status=order.ORDER_CONFIRMED
                   #order_obj.total_cart_amount=total
                    order_obj.save()
                    staus_message="your order processed. items will be delivered within 2 days"
                    messages.success(request,staus_message)
               elif not order_obj.added_items.exists():  # Assuming 'added_items' is the related name for items in the order
                    staus_message="cart is empty" 
                    messages.warning(request,staus_message)
             
               else:
                    staus_message="unable to process. no items in cart"
                    messages.error(request,staus_message)
          except Exception as e:
               staus_message="unable to process. no items in carts"
               messages.error(request,staus_message)
               
     
     return redirect('cart')          


"""def checkout(request):
    if request.method == 'POST':
        user = request.user
        customer = user.customer_profile
        
        total = float(request.POST.get('total', 0))  # Default to 0 if 'total' is missing
        
        # Get the order or return a 404 if it does not exist
        order_obj = get_object_or_404(order, owner=customer, order_status=order.CART_STAGE)
        
        if order_obj:
            order_obj.order_status = order.ORDER_CONFIRMED
            order_obj.save()
            status_message = "Your order has been processed. Items will be delivered within 2 days."
            messages.success(request, status_message)
        else:
            status_message = "Unable to process. No items in cart."
            messages.error(request, status_message)
    
    return redirect('cart')"""


@login_required(login_url='customer_login')
def orders(request):
     user=request.user
     customer, _ = Customer.objects.get_or_create(user=user, defaults={'name': user.username, 'address': 'Not provided'})
     all_orders=order.objects.filter(owner=customer).exclude(order_status=order.CART_STAGE)
     context={'allorder':all_orders}
     
     return render(request,'orders.html',context)  