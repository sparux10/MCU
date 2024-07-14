from rest_framework import serializers
from .models import Order, OrderProduct

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['id', 'product', 'quantity', 'color_size']

class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'created_at', 'updated_at']
from rest_framework import serializers
from .models import Cart, CartProduct

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'quantity', 'color_size']

class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'created_at', 'updated_at']
