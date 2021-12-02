from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# this was taken from my django ecommerce database file.

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.TextField(max_length=11)
    address = models.TextField()
    slug = models.SlugField(unique=True)

class Product(models.Model):
    product_name= models.CharField(max_length=24)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    product_price = models.FloatField()
    image1 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image2 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image3 = models.FileField(blank=True, null=True, upload_to='uploads/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    image1 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image2 = models.FileField(blank=True, null=True, upload_to='uploads/')
    slug = models.SlugField(unique=True)

class ProductCategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    # category_id= models.ForeignKey(Category, on_delete=models.CASCADE)







