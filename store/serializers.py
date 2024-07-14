from rest_framework import serializers
from .models import Product, Color, Size, Category, ColorSize

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
        fields = ['id', 'name', 'description', 'categoury_img', 'created_at', 'user']


class ColorSizeSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    size = SizeSerializer()

    class Meta:
        model = ColorSize
        fields = ['id', 'color', 'size']

class ProductSerializer(serializers.ModelSerializer):
    color_sizes = ColorSizeSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'discount', 'brand', 'ratings', 'stock', 'product_img', 'category', 'created_at', 'user', 'color_sizes']

    def create(self, validated_data):
        color_sizes_data = validated_data.pop('color_sizes', [])
        product = Product.objects.create(**validated_data)

        for color_size_data in color_sizes_data:
            color_data = color_size_data['color']
            size_data = color_size_data['size']

            color, created = Color.objects.get_or_create(**color_data)
            size, created = Size.objects.get_or_create(**size_data)

            color_size, created = ColorSize.objects.get_or_create(color=color, size=size)
            product.color_sizes.add(color_size)

        return product

    def update(self, instance, validated_data):
        color_sizes_data = validated_data.pop('color_sizes', [])
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

        # Update color_sizes
        instance.color_sizes.clear()
        for color_size_data in color_sizes_data:
            color_data = color_size_data['color']
            size_data = color_size_data['size']

            color, created = Color.objects.get_or_create(**color_data)
            size, created = Size.objects.get_or_create(**size_data)

            color_size, created = ColorSize.objects.get_or_create(color=color, size=size)
            instance.color_sizes.add(color_size)

        return instance