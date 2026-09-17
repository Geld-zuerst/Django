from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello World!, Currently ur in home page of my first backend project")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Hello World!, Currently ur in about page of my first backend project")

def contact(request):
    return render(request, 'contact.html')

def gallary(request):
    return render(request, 'gallary.html')

def aminities(request):
    return render(request, 'aminities.html')

def weddings(request):
    return render(request, 'weddings.html')