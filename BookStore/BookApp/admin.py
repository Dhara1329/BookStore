from django.contrib import admin
from BookApp.models import *
# Register your models here.

class AdminImages(admin.ModelAdmin):
	list_display = ['Book_Name','Book_Price','Book_Image']

admin.site.register(UserDetailsModel)
admin.site.register(BookDetailsModel)