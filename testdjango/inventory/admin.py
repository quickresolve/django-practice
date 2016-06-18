from django.contrib import admin

from .models import Item
#import Item model into admin

admin.site.register(Item)
#register Item with admin for CRUD functionality
