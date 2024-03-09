from django.db import models


# This code defines models for managing contacts, allowing the
# website to receive and store messages from site visitors.
class Contact(models.Model):
  name=models.CharField(max_length=25)
  email=models.EmailField()
  phonenumber=models.CharField(max_length=10)
  subject=models.CharField(max_length=30)
  message=models.TextField()

  def __str__(self):
    return self.name
  
# This code defines models for managing blog contents.
class Blogs(models.Model):
  title=models.CharField(max_length=60)
  decription=models.TextField()
  authname=models.CharField(max_length=20)
  img=models.ImageField(upload_to='blog',blank=True,null=True)
  timeStamp=models.DateTimeField(auto_now_add=True,blank=True,null=True)

  def __str__(self):
    return self.title
  
class Training(models.Model):
  fullname=models.CharField(max_length=60)
  usn=models.CharField(max_length=60)
  email=models.CharField(max_length=60)
  highest_qualification=models.CharField(max_length=100)
  offers_status=models.CharField(max_length=60)
  start_date=models.CharField(max_length=60)
  end_date=models.CharField(max_length=60)
  proj_report=models.CharField(max_length=60)
  timeStamp=models.DateTimeField(auto_now_add=True,blank=True,null=True)
  
  def __str__(self):
    return self.usn



