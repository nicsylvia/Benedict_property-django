from django.urls import path
from Sylvia_app import views

urlpatterns = [
    path('', views.about_detail, name ='about_detail'),
    path('product-detail/', views.product_detail, name ='product_detail'),
    path('product-list1/', views.product_list1, name='product_list1'),
    path('product-list2/', views.product_list2, name='product_list2'),
]