from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categary_name',)}
    list_display = ('categary_name','slug')
    
admin.site.register(Category, CategoryAdmin)