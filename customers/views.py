from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


"""def customer_login(request):
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
         
            user=authenticate(username='username',password='password')
            
            if user:
                login(request,user)
                return redirect('productslist')
                print("User authenticated")
            else:
               print("Authentication failed")
              
              
               messages.error(request,"invalid user")
    

    return render(request,'customer_account.html',context)"""


def customer_login (request):
   user=None
   error_message=None
   bug_message=None
   if request.POST and 'register' in request.POST:
      username=request.POST['username']
      password=request.POST['password']
      email=request.POST.get('email')
      address=request.POST.get('address')
      phone=request.POST.get('phone')
      print(username,password)
      try:
         user=User.objects.create_user(username=username,password=password,email=email)
         customer.objects.create(user=user,address=address,phone=phone)
      except Exception as e:
         error_message=str(e)
   if request.POST and 'login' in request.POST: 
      username=request.POST.get('username')
      password=request.POST['password']
      user=authenticate(username=username,password=password)
      
      if user:
         print(username,password)
         login(request,user)
         return redirect('productslist')

      else:
         bug_message='invalid credentials'  

   return render(request,'customer_account.html',{'user':user,'error_message':error_message,'bug_message':bug_message})


   


def signout(request):
    logout(request)
    return redirect('products')

