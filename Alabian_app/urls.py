from django.urls import path
from Alabian_app import views

app_name = 'Alabian_app'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]