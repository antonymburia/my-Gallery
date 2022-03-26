from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import User,Image,Category,Location
from django.core.exceptions import DoesNotExist


# Create your views here.

def pics(request):
    category = Category.get_categories()
    pictures = Image.all_pics()
    location_pics = Location.get_location()

    return render(request,'images.html',{'pictures': pictures, 'category': category, 'location_pics':location_pics })


