from django.shortcuts import render
from django.http import HttpResponse
from app import templates


# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request,'create.html')

def store(request):
    return render(request,'home.html')