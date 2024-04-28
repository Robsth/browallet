from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import TransactionViewSet, WalletViewSet

router = DefaultRouter()
router.register(r'wallets', WalletViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
