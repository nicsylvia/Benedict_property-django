from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'public/frontend/index.html')

def about(request):
    team= Team_Member.objects.all()
    return render(request, 'public/frontend/about.html', {'team': team})
   
def contact(request):
    return render(request, 'public/frontend/contact.html')
