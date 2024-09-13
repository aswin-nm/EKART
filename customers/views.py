from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def customer_login(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            user=User.objects.create_user(username=username,password=password,email=email)
          
            print(user)
       
            customer.objects.create(user=user,address=address,phone=phone)
            success_message="user created successfully"
            messages.success(request,success_message)
            #return redirect('products')
        except Exception as e:
            error_message="username already exists"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
            context['register']=False
            
        
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = User.objects.get(username='rony')
            print(user.is_active)  # Should be True
 
            user=authenticate(username='username',password='password')
            
            if user:
               # login(request,user)
             
                print("User authenticated")
            else:
               print("Authentication failed")
              
                #return redirect('productslist')
               
           # else:
              
               #messages.error(request,"invalid user")
    

    return render(request,'customer_account.html',context)

def signout(request):
    logout(request)
    return redirect('products')

