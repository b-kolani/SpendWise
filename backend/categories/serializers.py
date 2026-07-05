from rest_framework import serializers
from .models import Category

class   CategoryReadSerializer(serializers.ModelSerializer):

    class   Meta:
        model = Category
        # fields = "__all__"
        fields = (
            "id",
            "name",
            "color",
            "icon",
        )

class   CategoryWriteSerializer(serializers.ModelSerializer):

    class   Meta:
        model = Category
        # fields = "__all__"
        fields = (
            "id",
            "name",
            "color",
            "icon",
        )

# class   CategorySerializer(serializers.ModelSerializer):

#     class   Meta:
#         model = Category
#         fields = "__all__"
#         read_only_fields = ("user",)
