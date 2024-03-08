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
  





