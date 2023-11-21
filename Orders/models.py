from django.db import models

class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    seats = models.PositiveIntegerField(help_text="Number of seats at the table")

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    name_zh = models.CharField(max_length=100)  # Chinese name
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Dish Model
class Dish(models.Model):
    name = models.CharField(max_length=100)
    name_zh = models.CharField(max_length=100)  # Chinese name
    ingredients = models.TextField()
    ingredients_zh = models.TextField()  # Chinese ingredients
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

# DishImage Model
class DishImage(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='dishes/')

    def __str__(self):
        return self.dish.name + " Image"

# Order Model
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Total cost of the order

    def __str__(self):
        return f"Order {self.id}"

# OrderItem Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)  # Price at the time of order
    total = models.DecimalField(max_digits=10, decimal_places=2)  # unit_price * quantity

    def __str__(self):
        return f"{self.quantity} x {self.dish.name}"
