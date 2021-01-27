from django.shortcuts import render
from .models import Product
from .models import People


# Create your views here.
def products(request):
    context = {}
    context['products'] = Product.objects.all()
    return render(request, 'mywebsite/products.html', context) 
 
    
def people(request):
    context = {}
    context['peoples'] = People.objects.all()
    return render(request, 'mywebsite/people.html', context)

def home(request):
    context = {}
    return render(request, 'mywebsite/home.html', context)

    
def contactus(request):
    context = {}
    return  render(request, 'mywebsite/contactus.html', context)

