from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    users = {
        "name":"Shravan",
        "place":"Mala",
        "phone":8590929768,
        "number":30
    }
    return render(request,'index.html',users)
def about(request):
    return render(request,'about.html')
# Create your views here.
def places(request):
    return HttpResponse("Places")
def booking(request):
    return HttpResponse("Booking")
