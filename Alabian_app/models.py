from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# this was taken from my django ecommerce database file.

class User(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    password = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.TextField(max_length=11)
    address = models.TextField()
   
    def __str__(self):
        return self.name

class Product(models.Model):
    product_name= models.CharField(max_length=24)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    product_price = models.FloatField()
    image1 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image2 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image3 = models.FileField(blank=True, null=True, upload_to='uploads/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    def get_image1(self):
        if self.image1:
            return self.image1.url

    def get_image2(self):
        if self.image2:
            return self.image2.url

    def get_image3(self):
        if self.image3:
            return self.image3.url

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    image1 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image2 = models.FileField(blank=True, null=True, upload_to='uploads/')
    class Meta():
        verbose_name_plural = 'P-category'
    def __str__(self):
        return self.category_name

    def get_image1(self):
        if self.image1:
            return self.image1.url

    def get_image2(self):
        if self.image2:
            return self.image2.url

class ProductCategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    # category_id= models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Product_Category

    class Meta():
        verbose_name_plural = 'Product-Category'

class TeamMember(models.Model):
    teamMember_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    profile = models.FileField(blank=True, null=True, upload_to='uploads/')
    Bio = models.TextField()

    class Meta():
        verbose_name_plural = 'Team_Member'

    def __str__(self):
        return self.teamMember_name

    def image(self):
        if self.profile:
            return self.profile.url