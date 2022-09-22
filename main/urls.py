from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name ="home"),
    path('product/',views.product, name="product"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
]
