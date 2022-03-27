from django.contrib import admin
from .models import User,Category,Image,Location

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)