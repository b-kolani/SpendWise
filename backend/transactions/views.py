from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)

from .models import Transaction
from .serializers import (
    TransactionReadSerializer,
    TransactionWriteSerializer,
)

from .filters import TransactionFilter


class TransactionViewSet(ModelViewSet):
    # serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]

    filterset_class = TransactionFilter

    ordering_fields = [
        "date",
        "amount",
        "title"
    ]

    ordering = ["-date"]

    search_fields = [
        "title",
        "description",
    ]

    # Return the class to use for the serializer.
    # Thsi function will inference the serializer to use
    # base on the action
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TransactionReadSerializer
        
        return TransactionWriteSerializer
    
    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)

        # Optional filters via query params
        # transaction_type = self.request.query_params.get('type')
        # category_id = self.request.query_params.get('category')

        # if transaction_type:
        #     queryset = queryset.filter(type=transaction_type)
        # if category_id:
        #     queryset = queryset.filter(category_id=category_id)
    
        return queryset
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    