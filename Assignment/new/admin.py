from django.contrib import admin
from .models import User
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display = ['username','email','password','full_name','age','gender']

admin.site.register(User,AdminUser)