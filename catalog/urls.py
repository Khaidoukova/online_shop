from django.contrib import admin
from django.urls import path

from catalog.views import home, contacts, index

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('index/', index)
]
