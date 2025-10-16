from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
# Create your views here.
def places(request):
    return render(request,'places.html')
def booking(request):
    return render(request,'booking.html')
def contacts(request):
    return render(request,'contact.html')