from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import User,Image,Category,Location
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def pics(request):
    category = Category.get_categories()
    pictures = Image.all_images ()
    location_pics = Location.get_location()

    return render(request,'images.html',{'pictures': pictures, 'category': category, 'location_pics':location_pics })

def single_pic(request,id):
    try:
        image = Image.objects.get(id = id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"single_image.html", {"image":image})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_pics = Image.search_by_name(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{"message":message,"image":searched_pics})

    else:
        message = "field cannot be empty"
        return render(request,'search.html',{"message":message})

def viewPics_by_location(request,location):
    locationimages = Image.view_pictures_by_location(location)
    return render(request,"location_images.html",{"locationimages":locationimages})


def viewPics_by_category(request,category):
    photos =Image.view_pictures_by_category(category)
    return render (request,'categories.html',{"photos":photos})

