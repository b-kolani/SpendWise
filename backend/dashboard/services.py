from decimal import Decimal

from django.db.models import Sum, F
from django.db.models.functions import TruncMonth

from transactions.models import Transaction

class   DashboardService:

    def __init__(
        self,
        user,
        date_after,
        date_before
    ):
        self.user = user
        self.date_after = date_after
        self.date_before = date_before
    
    def _get_transactions(self):
        queryset = Transaction.objects.filter(
            user=self.user
        )

        if self.date_after:
            queryset = queryset.filter(
                date__gte = self.date_after
            )
        
        if self.date_before:
            queryset = queryset.filter(
                date__lte = self.date_before
            )

        return queryset

    def get_total_income(self):
        return (
            self._get_transactions()
            .filter(
                type=Transaction.TransactionType.INCOME
            )
            .aggregate(
                total=Sum("amount")
            )["total"] or Decimal("0")
        )

    def get_total_expense(self):
        return (
            self._get_transactions()
            .filter(
                type=Transaction.TransactionType.EXPENSE
            )
            .aggregate(
                total=Sum("amount")
            )["total"] or Decimal("0")
        )

    def get_transactions_count(self):
        return  (
            self._get_transactions()
            .count()
        )
    
    def get_expenses_by_category(self):
        return (
            self._get_transactions()
            .filter(
                type = Transaction.TransactionType.EXPENSE
            )
            .values(category_=F("category__name"))
            .annotate(total=Sum("amount"))
            .order_by("-total")
        )

    def get_monthly_expense(self):
        return (
            self._get_transactions()
            .filter(
                type = Transaction.TransactionType.EXPENSE
            )
            .annotate(month=TruncMonth("date"))
            .values("month")
            .annotate(total=Sum("amount"))
            .order_by("month")
        )
    
    def get_incomes_by_category(self):
        return (
            self._get_transactions()
            .filter(
                user=self.user,
                type=Transaction.TransactionType.INCOME
            )
            .values(category_=F("category__name"))
            .annotate(total=Sum("amount"))
            .order_by("-total")
        )
    
    def get_monthly_income(self):
        return (
            self._get_transactions()
            .filter(
                user = self.user,
                type = Transaction.TransactionType.INCOME
            )
            .annotate(month=TruncMonth("date"))
            .values("month")
            .annotate(total=Sum("amount"))
            .order_by("month")
        )
    
    def get_balance(self):
        income = self.get_total_income()
        expense = self.get_total_expense()

        return income - expense
    
    def get_dashboard(self):
        return {
            "total_income": self.get_total_income(),
            "total_expense": self.get_total_expense(),
            "balance": self.get_balance(),
            "transactions_count": self.get_transactions_count(),
            "expenses_by_category": self.get_expenses_by_category(),
            "monthly_expense": self.get_monthly_expense(),
            "incomes_by_category": self.get_incomes_by_category(),
            "monthly_income": self.get_monthly_income()
        }