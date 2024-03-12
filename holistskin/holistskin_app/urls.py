from django.urls import path
from  holistskin_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('address',views.address,name='address'),
    path('blog',views.handleblog,name='handleblog'),
    path('buttons',views.buttons,name='buttons'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('confirmation',views.confirmation,name='confirmation'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('empty_cart',views.empty_cart,name='empty_cart'),
    path('faq',views.faq,name='faq'),
    path('index',views.index,name='index'),
    path('forget_password',views.forget_password,name='forget_password'),
    path('order',views.order,name='order'),
    path('pricing',views.pricing,name='pricing'),
    path('product_single',views.product_single,name='product_single'),
    path('profile_details',views.profile_details,name='profile_details'),
    path('purchase_confirmation',views.purchase_confirmation,name='purchase_confirmation'),
    path('shop_sidebar',views.shop_sidebar,name='shop_sidebar'),
    path('shop',views.shop,name='shop'),
    path('signin',views.signin,name='signin'),
    path('trainingdetails',views.trainingdetails,name='trainingdetails'),
    path('Contact',views.Contact,name='contact'),
]