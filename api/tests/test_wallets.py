from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal

from api.models import Wallet


class WalletBaseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()


class WalletUpdateDeleteTests(WalletBaseTestCase):
    def test_update_wallet_not_allowed(self):
        wallet = Wallet.objects.create(label='Test Wallet', balance=Decimal('100.00'))
        wallet_url = f'/api/wallets/{wallet.id}/'

        update_response = self.client.patch(wallet_url, {'label': 'Updated Wallet'})
        self.assertEqual(update_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_wallet_not_allowed(self):
        wallet = Wallet.objects.create(label='Test Wallet', balance=Decimal('100.00'))
        wallet_url = f'/api/wallets/{wallet.id}/'

        delete_response = self.client.delete(wallet_url)
        self.assertEqual(delete_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
