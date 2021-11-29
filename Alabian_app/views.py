from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is the Home Page😀')

def about(request):
    return HttpResponse('Find out About Us Here😊')

def contact(request):
    return HttpResponse('Contact me here🤩')