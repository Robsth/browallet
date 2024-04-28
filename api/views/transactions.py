from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api.exceptions import InsufficientFunds
from api.models import Transaction
from api.serializers import TransactionSerializer
from api.services.transactions import create_transaction


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['wallet', 'txid']
    ordering_fields = ['amount']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except InsufficientFunds as e:
            raise ValidationError({'amount': [str(e)]})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        wallet_id = serializer.validated_data['wallet'].id
        amount = serializer.validated_data['amount']
        create_transaction(wallet_id, amount)
