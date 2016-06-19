from django.shortcuts import render
from django.http import Http404 #returns both 404 page and HttpResponse object

from inventory.models import Item
#import item model to pass to routes

#route for index page
def index(request):
    items = Item.objects.exclude(amount=0)
    #pass items that are in stock to index page
    return render(request, 'inventory/index.html', {
        'items': items,

    })

    # return HttpResponse('<p>In index view</p>') - Alternative to render


#route for item_detail page
def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist!')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })

    # return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id)) - Alternative to render
