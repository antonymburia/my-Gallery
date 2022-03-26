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

def single_pic(request,id):
    try:
        pic = Image.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single_image.html", {"pic":pic})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_pics = Image.search_by_name(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{"message":message,"image":searched_pics})

    else:
        message = "field cannot be empty"
        return render(request,'search.html',{"message":message})


