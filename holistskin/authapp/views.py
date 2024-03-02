from django.shortcuts import render

# Create your views here.
def signin(request):
  return render(request,'signin.html')

def handleLogin(request):
  return render(request,'handleLogin.html')

def handleLogout(request):
  return render(request,'handleLogout.html')

def handleForget_password(request):
  return render(request,'handleForget_password.html')