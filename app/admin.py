from django.contrib import admin
from .models import Category, ToDo


admin.site.register(ToDo)
admin.site.register(Category)
