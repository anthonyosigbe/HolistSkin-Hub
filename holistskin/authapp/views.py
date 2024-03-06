from django.shortcuts import render

# Create your views here.
def signin(request):
  return render(request,'signin.html')

def handleLogin(request):
  return render(request,'login.html')

def handleLogout(request):
  return render(request,'logout.html')

def handleForget_password(request):
  return render(request,'forget_password.html')