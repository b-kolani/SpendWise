from rest_framework import serializers
from .models import Transaction

class   TransactionSerializer(serializers.ModelSerializer):

    class   Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ("user",)

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "The amount must be greater than 0."
            )
        return value

    def validate_category(self, category):
        user = self.context['request'].user

        if category.user != user:
            raise serializers.ValidationError(
                "This category doesn't belong to you."
            )
        
        return category
