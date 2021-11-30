from django.urls import path
from Alabian_app import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]