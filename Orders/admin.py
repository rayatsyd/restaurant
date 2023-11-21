from django.contrib import admin
from .models import Category, Dish, DishImage, Order, OrderItem

# Registering the models for the admin interface
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(DishImage)
admin.site.register(Order)
admin.site.register(OrderItem)
