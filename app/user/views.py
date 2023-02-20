"""
Views for the user API
"""
from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """
    Create a mew user in the database
    """
    serializer_class = UserSerializer
