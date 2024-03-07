from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Created views that links backend to front end for login authentications.
def signin(request):
  if request.method=="POST":
    get_full_name=request.POST.get('full_name')
    get_email=request.POST.get('email')
    get_password=request.POST.get('pass1')
    get_confirm_password=request.POST.get('pass2')

    if get_password != get_confirm_password:
      messages.info(request,'Password does not match')
      return redirect('/auth/signin/')
    
    try:
      if User.objects.get(username=get_email):
        messages.warning(request,"Email Already Taken")
        return redirect('/auth/signin/')
      
    except Exception as Identifier:
      pass

    myuser=User.objects.create_user(get_email,get_email,get_password)
    myuser.save()
    messages.success(request,'User Created Please Login')

    return redirect('/auth/login/')

  

  return render(request,'signin.html')

def handleLogin(request):
  return render(request,'login.html')

def handleLogout(request):
  return render(request,'logout.html')

def handleForget_password(request):
  return render(request,'forget_password.html')