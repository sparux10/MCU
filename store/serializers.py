from rest_framework import serializers
from .models import *

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'color_name']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'size_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'category_img', 'created_at', 'user']

class ProductColorSizeSerializer(serializers.ModelSerializer):
    color_id = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), source='color')
    size_id = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all(), source='size')
    color_name = serializers.CharField(source='color.color_name', read_only=True)
    size_name = serializers.CharField(source='size.size_name', read_only=True)

    class Meta:
        model = ProductColorSize
        fields = ['id','color_id', 'color_name', 'size_id','size_name']



class ProductSerializer(serializers.ModelSerializer):
    product_colors_sizes = ProductColorSizeSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'discount', 'brand', 'ratings', 'stock', 'product_img', 'category', 'created_at', 'user', 'product_colors_sizes']

    def create(self, validated_data):
        product_colors_sizes_data = validated_data.pop('product_colors_sizes', [])
        product = Product.objects.create(**validated_data)

        for color_size_data in product_colors_sizes_data:
            color = color_size_data['color']
            size = color_size_data['size']
            ProductColorSize.objects.create(product=product, color=color, size=size)

        return product

    def update(self, instance, validated_data):
        product_colors_sizes_data = validated_data.pop('product_colors_sizes', [])
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.ratings = validated_data.get('ratings', instance.ratings)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.product_img = validated_data.get('product_img', instance.product_img)
        instance.category = validated_data.get('category', instance.category)
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        # Update product_colors_sizes
        for color_size_data in product_colors_sizes_data:
            color = color_size_data['color']
            size = color_size_data['size']
            ProductColorSize.objects.create(product=instance, color=color, size=size)
        
        return instance