from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from main.models import *
from django.contrib import messages


# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)
    #return HttpResponse("This is the home page")

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html', context)

def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'product.html', context)


def cart(request):
    context = {}
    return render(request, 'main/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'main/checkout.html', context)


