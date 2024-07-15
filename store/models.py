from django.db import models
from superuser.models import MyUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, default="", blank=False)
    description = models.TextField(max_length=1000, default="", blank=False)
    category_img = models.ImageField(upload_to='category_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL, related_name='categories')

    def __str__(self):
        return self.name

class Color(models.Model):
    color_name = models.CharField(max_length=200, default="", blank=False)

    def __str__(self):
        return self.color_name

class Size(models.Model):
    size_name = models.CharField(max_length=200, default="", blank=False)

    def __str__(self):
        return self.size_name

class Product(models.Model):
    name = models.CharField(max_length=200, default="", blank=False)
    description = models.TextField(max_length=1000, default="", blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    brand = models.CharField(max_length=200, default="", blank=False)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    product_img = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL, related_name='products')

    def __str__(self):
        return self.name
    
class ProductColorSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_colors_sizes')
    color = models.ForeignKey(Color, null=True, on_delete=models.SET_NULL, related_name='product_colors_sizes')
    size = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL, related_name='product_colors_sizes')

    def __str__(self):
        return f"{self.color.color_name} - {self.size.size_name}"
