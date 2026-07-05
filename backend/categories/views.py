from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Category
from .serializers  import (
    CategoryReadSerializer,
    CategoryWriteSerializer
)

# Create your views here.
class   CategoryViewSet(ModelViewSet):
    # serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return  CategoryReadSerializer

        return CategoryWriteSerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
