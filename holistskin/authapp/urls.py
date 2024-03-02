from django.urls import path
from  authapp import views


urlpatterns = [
    path('signin/',views.signin,name='signin'),
    path('login/',views.handleLogin,name='handleLogin'),
    path('logout/',views.handleLogout,name='handleLogout'),
    path('forget_password/',views.handleForget_password,name='forget_password'),
   
]