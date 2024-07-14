from django.db import models
from superuser.models import *

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, default="",blank=False)
    description = models.TextField(max_length=1000, default="",blank=False)
    categoury_img = models.ImageField(upload_to='category_images/',null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)

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

class ColorSize(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.color.color_name} - {self.size.size_name}"

class Product(models.Model):
    name = models.CharField(max_length=200, default="", blank=False)
    description = models.TextField(max_length=1000, default="", blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    brand = models.CharField(max_length=200, default="", blank=False)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    product_img = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    color_sizes = models.ManyToManyField(ColorSize)  # إضافة العلاقة "many-to-many"

    def __str__(self):
        return self.name