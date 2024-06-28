from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "pyaar/index.html",{})

def about(request):
    return render(request, "pyaar/about.html",{})

def blog(request):
    return render(request, "pyaar/blog.html",{})

def contact(request):
    return render(request, "pyaar/contact.html",{})

def gallery(request):
    return render(request, "pyaar/gallery.html",{})

def donate(request):
    return render(request, "pyaar/donate.html",{})

def event(request):
    return render(request, "pyaar/event.html",{})

def causes(request):
    return render(request, "pyaar/causes.html",{})