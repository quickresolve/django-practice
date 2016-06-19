"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from inventory import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'), #sets root to index view
    url(r'^item/(?P<id>\d+)/', views.item_detail, name = 'item_detail'), #sets item with id num to item_detail view
    url(r'^admin/', admin.site.urls), #sets /admin to admin views
]
