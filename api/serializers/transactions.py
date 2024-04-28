from rest_framework import serializers

from api.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['wallet', 'txid', 'amount']
        read_only_fields = ['txid']

    @staticmethod
    def validate_amount(value):
        if value == 0:
            raise serializers.ValidationError("Amount cannot be zero.")
        return value
