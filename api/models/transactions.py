import uuid

from django.db import models

from api.models.wallets import Wallet


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, related_name='transactions', on_delete=models.PROTECT)
    txid = models.CharField(max_length=36, unique=True, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.txid:
            self.txid = str(uuid.uuid4())
        super().save(*args, **kwargs)
