from django.contrib import admin

from .models import Item
#import Item model into admin

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']

#update list_display by adding ItemAdmin class to overide default

admin.site.register(Item, ItemAdmin)
#register Item with admin for CRUD functionality
#include ItemAdmin in argument
