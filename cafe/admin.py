# admin.py
from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'price', 'image')  # Changed 'image_url' to 'image'
    list_filter = ('category',)

admin.site.register(Item, ItemAdmin)
