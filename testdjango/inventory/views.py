from django.shortcuts import render
from django.http import HttpResponse

#route for index page
def index(request):
    return HttpResponse('<p>In index view</p>')


#route for item_detail page
def item_detail(request, id):
    return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))
