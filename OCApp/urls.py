from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CartViewSet

# Define router
router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'cart', CartViewSet)

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]

