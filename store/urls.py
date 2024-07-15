from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ColorViewSet, SizeViewSet, ProductColorSizeViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'productcolorsizes', ProductColorSizeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
