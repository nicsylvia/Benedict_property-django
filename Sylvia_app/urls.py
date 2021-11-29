from django.urls import path
from Sylvia_app import views

urlpatterns = [
    path('', views.login, name ='login'),
    path('register/', views.register, name ='register'),
    path('services/', views.services, name='services'),
]