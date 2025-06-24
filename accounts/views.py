from django.contrib.auth import  get_user_model
from .serializers import RegisterSerializer
from rest_framework import generics

user = get_user_model()

class RegisterView(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = RegisterSerializer
