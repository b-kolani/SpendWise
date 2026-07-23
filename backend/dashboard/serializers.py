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
