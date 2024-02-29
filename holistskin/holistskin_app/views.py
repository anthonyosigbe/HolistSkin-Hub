from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,'index.html')

def login(request):
  return render(request,'login.html')

def about(request):
  return render(request,'about.html')

def address(request):
  return render(request,'address.html')

def alerts(request):
  return render(request,'alerts.html')

def blog_full_width(request):
  return render(request,'blog_full_width.html')


