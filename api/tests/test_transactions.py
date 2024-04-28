from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal

from api.models import Wallet
from api.exceptions import InsufficientFunds
from api.services.transactions import create_transaction


class TransactionBaseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet = Wallet.objects.create(label='Test Wallet', balance=Decimal('100.00'))

    def create_transaction(self, amount):
        return self.client.post('/api/transactions/', {'wallet': self.wallet.id, 'amount': str(amount)})


class TransactionAPITests(TransactionBaseTestCase):
    def test_create_transaction(self):
        response = self.create_transaction('50.00')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_transaction_insufficient_funds(self):
        response = self.create_transaction('-150.00')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TransactionValidationTests(TransactionBaseTestCase):
    def test_transaction_with_invalid_amount(self):
        response = self.create_transaction('not_a_number')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_zero_amount_transaction(self):
        response = self.create_transaction('0.00')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_transaction_that_zeroes_balance(self):
        response = self.create_transaction('-100.00')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal('0.00'))


class TransactionServiceTests(TransactionBaseTestCase):
    def test_create_transaction_insufficient_funds(self):
        with self.assertRaises(InsufficientFunds):
            create_transaction(self.wallet.id, Decimal('-150.00'))
