from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import UserCreateSerializer, UserManageSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = get_user_model().objects.all()
    permission_classes = []
    authentication_classes = []


class UserManageView(generics.RetrieveUpdateAPIView):
    serializer_class = UserManageSerializer
    queryset = get_user_model().objects.prefetch_related("favorites")
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user
