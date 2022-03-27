from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.pics,name='pics'),
    url(r'^single_pic/(\d+)',views.single_pic),
    url(r'^search/',views.search_results),
    url(r'^location/(\d+)',views.viewPics_by_location),
    url(r'^category/(\d+)',views.viewPics_by_category)
    ]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)