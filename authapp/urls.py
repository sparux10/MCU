# authapp/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('logout/', Logout.as_view(), name='token_blacklist'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
