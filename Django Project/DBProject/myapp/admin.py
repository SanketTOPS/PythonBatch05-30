from django.contrib import admin
from .models import userData

# Register your models here.

class userdataAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','mobile','address']

admin.site.register(userData,userdataAdmin)