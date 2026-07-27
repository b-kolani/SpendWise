from rest_framework import serializers

class CategoryExpenseSerializer(serializers.Serializer):
    category_ = serializers.CharField()
    total = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

class   MonthlyExpenseSerializer(serializers.Serializer):
    month = serializers.DateField()
    total = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

class   CategoryIncomeSerializer(serializers.Serializer):
    category_ = serializers.CharField()
    total = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

class   MonthlyIncomeSerializer(serializers.Serializer):
    month = serializers.DateField()
    total = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

class   DashboardSerializer(serializers.Serializer):
    total_income = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    total_expense = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    balance = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    transactions_count = serializers.IntegerField()

    expenses_by_category = CategoryExpenseSerializer(
        many=True
    )

    monthly_expense = MonthlyExpenseSerializer(
        many=True
    )

    incomes_by_category = CategoryIncomeSerializer(
        many=True
    )

    monthly_income = MonthlyIncomeSerializer(
        many=True
    )

class   DashboardFilterSerializer(serializers.Serializer):
    date_after = serializers.DateField(
        required=False
    )

    date_before = serializers.DateField(
        required=False
    )

    def validate(self, attrs):
        self.date_after = attrs.get("date_after")
        self.date_before = attrs.get("date_before")

        if (
            self.date_after 
            and self.date_before
            and self.date_after > self.date_before
        ):
            raise serializers.ValidationError(
                "date_after should be before date_before."
            )
        return attrs