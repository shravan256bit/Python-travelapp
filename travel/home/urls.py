from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('about',views.about,name="about"),
    path('places',views.places,name="place"),
    path('booking',views.booking,name="booking"),
    path('contacts',views.contacts,name="contacts"),
    

]
