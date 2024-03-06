from django.shortcuts import render

# Creating views that dynamically render each HTML page directly from the database..
def index(request):
  return render(request,'index.html')

def login(request):
  return render(request,'login.html')

def about(request):
  return render(request,'about.html')

def address(request):
  return render(request,'address.html')

def blog_single(request):
  return render(request,'blog_single.html')

def buttons(request):
  return render(request,'buttons.html')

def cart(request):
  return render(request,'cart.html')

def checkout(request):
  return render(request,'checkout.html')

def coming_soon(request):
  return render(request,'coming_soon.html')

def confirmation(request):
  return render(request,'confirmation.html')

def confirmation(request):
  return render(request,'confirmation.html')

def contact(request):
  return render(request,'contact.html')

def dashboard(request):
  return render(request,'dashboard.html')

def empty_cart(request):
  return render(request,'empty_cart.html')

def faq(request):
  return render(request,'faq.html')

def forget_password(request):
  return render(request,'forget_password.html')

def order(request):
  return render(request,'order.html')

def pricing(request):
  return render(request,'pricing.html')

def product_single(request):
  return render(request,'product_single.html')

def profile_details(request):
  return render(request,'profile_details.html')

def purchase_confirmation(request):
  return render(request,'purchase_confirmation.html')

def shop_sidebar(request):
  return render(request,'shop_sidebar.html')

def shop(request):
  return render(request,'shop.html')

def signin(request):
  return render(request,'signin.html')
