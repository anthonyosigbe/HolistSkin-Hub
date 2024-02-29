from django.urls import path
from  holistskin_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('address',views.address,name='address'),
    path('alerts',views.alerts,name='alerts'),
    path('blog_full_width',views.blog_full_width,name='blog_full_width'),

]