# authapp/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import BlacklistedToken

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView): 
    serializer_class = TokenObtainPairSerializer



class Logout(APIView):
    """
    أضف `access token` إلى قائمة سوداء JWT.

    Args:
        token (str): `access token` الذي تريد إبطاله.
    """
    def post(self, request):
        token = request.token
        try:
            token = BlacklistedToken(token)
            token.blacklist()
        except Exception as e:
        # تعامل مع أي استثناءات تحدث
            pass
