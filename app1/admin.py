from django.contrib import admin
from .models import Books

# Register your models here.
@admin.register(Books)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','name','author','price','genre','quantity','rating']
    list_display_links = ['name']
