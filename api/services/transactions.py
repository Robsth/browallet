from django.db import transaction

from api.exceptions import InsufficientFunds
from api.models import Wallet, Transaction


def create_transaction(wallet_id, amount):
    with transaction.atomic():
        wallet = Wallet.objects.select_for_update().get(id=wallet_id)
        new_balance = wallet.balance + amount
        if new_balance < 0:
            raise InsufficientFunds('There are not enough funds on your balance to complete the transaction')

        Transaction.objects.create(wallet=wallet, amount=amount)

        wallet.balance = new_balance
        wallet.save(update_fields=['balance'])
