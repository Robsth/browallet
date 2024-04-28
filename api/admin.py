from django.contrib import admin
from .models import Wallet, Transaction


class WalletAdmin(admin.ModelAdmin):
    list_display = ('label', 'balance', 'created_at', 'updated_at')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('txid', 'wallet', 'amount', 'created_at', 'updated_at')


admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
