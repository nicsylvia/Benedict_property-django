from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_detail(request):
    return render(request, 'public/frontend/about-detail.html')

def product_detail(request):
        return render(request, 'public/frontend/product-detail.html')

def product_list1(request):
    return render(request, 'public/frontend/product-list1.html')

def product_list2(request):
    return render(request, 'public/frontend/product-list2.html')
