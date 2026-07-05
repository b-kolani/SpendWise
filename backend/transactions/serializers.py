from rest_framework import serializers
from .models import Transaction

from categories.serializers import (
    CategoryReadSerializer,
    CategoryWriteSerializer
)

class   TransactionReadSerializer(serializers.ModelSerializer):
    category = CategoryReadSerializer(read_only=True)

    class   Meta:
        model = Transaction
        # fields = "__all__"
        fields = (
            "id",
            "title",
            "amount",
            "date",
            "description",
            "type",
            "category",
            "created_at",
            "update_at",
        )

class   TransactionWriteSerializer(serializers.ModelSerializer):

    class   Meta:
        model = Transaction
        # fields = "__all__"
        fields = (
            "id",
            "title",
            "amount",
            "date",
            "description",
            "type",
            "category",
            "created_at",
            "update_at",
        )
        read_only_fields = ("user",)

    def validate_amount(self, value):
        if value <= 0:
            raise   serializers.ValidationError(
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
        
    # This function handles a global validation 
    # (all data set or fields validations).
    # It concerns validations applied to 
    # many fields simultaneously.
    # For example we can check here if a transaction
    # marks as or with a income type uses a category 
    # field with expense value. This function will be 
    # fully implemented after.
    def validate(self, attrs):
        transaction_type = attrs.get("type")
        category = attrs.get("category")

        # Example of a future rule
        # if transaction_type == ... and category == ...
            # do something here

        return attrs

# class   TransactionSerializer(serializers.ModelSerializer):

#     class   Meta:
#         model = Transaction
#         fields = "__all__"
#         read_only_fields = ("user",)

#     def validate_amount(self, value):
#         if value <= 0:
#             raise serializers.ValidationError(
#                 "The amount must be greater than 0."
#             )
#         return value

#     def validate_category(self, category):
#         user = self.context['request'].user

#         if category.user != user:
#             raise serializers.ValidationError(
#                 "This category doesn't belong to you."
#             )
        
#         return category
