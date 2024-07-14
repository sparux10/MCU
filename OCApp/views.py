from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # يمكنك تغيير الصلاحيات كما تريد

from rest_framework import viewsets
from .models import Cart
from .serializer import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]  # يمكنك تغيير الصلاحيات كما تريد
