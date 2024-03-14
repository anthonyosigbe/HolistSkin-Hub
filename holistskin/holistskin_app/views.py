from django.shortcuts import render,redirect
from django.contrib import messages
from holistskin_app.models import Contact,Blogs,Training
# Imports for send emails
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage


# Creating views that dynamically render each HTML page directly from the database..
def index(request):
  return render(request,'index.html')

def login(request):
  return render(request,'login.html')

def about(request):
  return render(request,'about.html')

def address(request):
  return render(request,'address.html')

def handleblog(request):
  posts=Blogs.objects.all()
  context={"posts":posts}
  return render(request,'handleblog.html',context)

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

def Contact_view(request):
  if request.method=="POST":
    fname=request.POST.get('name')
    femail=request.POST.get('email')
    fphonenumber=request.POST.get('num')
    fsubject=request.POST.get('subject')
    fmessage=request.POST.get('message')
    query=Contact(name=fname,email=femail,phonenumber=fphonenumber,subject=fsubject,message=fmessage)
    query.save()

    messages.success(request,"Thank you for contacting us we will get back to you shortly")
    
    return redirect('/contact')

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

def trainingdetails(request):
  
  if not request.user.is_authenticated:
    messages.warning(request,"please Login to Access the training page")
    return redirect("/auth/login/")
  
  if request.method=="POST":
    fname=request.POST.get('name')
    femail=request.POST.get('email')
    fusn=request.POST.get('usn')
    fqualification=request.POST.get('hqualification')
    foffer=request.POST.get('offer')
    fstartdate=request.POST.get('startdate')
    fenddate=request.POST.get('enddate')
    fprojreport=request.POST.get('projreport')
    
# Converting to upper case letters.    
    fname=fname.upper()
    fusn=fusn.upper()
    fqualification=fqualification.upper()
    fprojreport=fprojreport.upper()
    foffer=foffer.upper()
    
# 
    check1=Training.objects.filter(usn=fusn)
    check2=Training.objects.filter(email=femail)
    
    if check1 or check2:
      messages.warning(request,"Details Already Registered, Login or request for Password Reset")
      return redirect('/index')
    
    query=Training(fullname=fname,usn=fusn,email=femail,highest_qualification=fqualification,offers_status=foffer,start_date=fstartdate,end_date=fenddate,proj_report=fprojreport)
    query.save()
    messages.success(request,"Form is Submitted Successfully")
    return redirect('/dashboard')
    
  return render(request,'training.html')