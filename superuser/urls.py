# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'role', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
