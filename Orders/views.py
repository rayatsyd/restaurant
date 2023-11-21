from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Category, Dish, Order, OrderItem, Table
from .serializers import CategorySerializer, DishSerializer, OrderSerializer, OrderItemSerializer, TableSerializer

# Create your views here.

# This is the main view for our app
def home(request):
    return render(request, 'index.html')

def generate_qr(request):
    # Any additional context you want to pass to the template can be included here
    context = {}
    return render(request, 'generate_qr.html', context)

# API views
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def get_queryset(self):
        queryset = Dish.objects.all()
        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
