from django.shortcuts import render
from urllib3 import request


# Create your views here.
def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

def events(request):
    return render(request,"events.html")