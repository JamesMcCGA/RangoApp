from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Link to the about page
    return HttpResponse("Rango says hey there partner! <br><a href='/rango/about/'>About</a>")

def about(request):
    # Link back to the index page
    return HttpResponse("Rango says here is the about page. <br><a href='/rango/'>Index</a>")