from django.db import models
from superuser.models import MyUser
from store.models import *

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.email}"
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    color_size = models.ForeignKey(ProductColorSize, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order {self.order.id} - Product {self.product.name}"

class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Cart for {self.user.email}"

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    color_size = models.ForeignKey(ProductColorSize, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Cart {self.cart.id} - Product {self.product.name}"
