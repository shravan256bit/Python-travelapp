from django.shortcuts import render
from django.http import HttpResponse
from .models import categories

def index(request):
    return render(request,'index.html')
def about(request):
    dict = {
        'category':categories.objects.all()
    }
    return render(request,'about.html',dict)
# Create your views here.
def places(request):
    return render(request,'places.html')
def booking(request):
    return render(request,'booking.html')
def contacts(request):
    return render(request,'contact.html')