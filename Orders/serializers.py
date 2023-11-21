from rest_framework import serializers
from .models import Category, Dish, DishImage, Order, OrderItem, Table


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImage
        fields = ('id', 'image')


class DishSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Dish
        fields = ('id', 'name', 'name_zh', 'ingredients', 'ingredients_zh', 'unit_price', 'image_url')

    def get_image_url(self, obj):
        # Assuming your image field in the DishImage model is named "image"
        return obj.images.first().image.url if obj.images.exists() else None


class OrderItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'created_at', 'completed', 'total_amount', 'items')


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'