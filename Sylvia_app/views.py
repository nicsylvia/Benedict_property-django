from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('<em>Login here Anytime Anyday</em>🔑🔐')

def register(request):
    return HttpResponse('<b>Register your Interest here</b>.')

def services(request):
    return HttpResponse('<h1>We offer a lot of Services. Come back here in the nearest future to view them.</h1>👌')
