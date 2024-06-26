from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from api.models.wallets import Wallet
from api.permissions import CreateReadPermission
from api.serializers.wallets import WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [CreateReadPermission]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['label']
    ordering_fields = ['label', 'balance']
