from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from categories.models import Category
from dashboard.services import DashboardService
from transactions.models import Transaction

User = get_user_model()

class   DashboardServiceTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="test",
            email="test@example.com",
            password="password123"
        )

        self.other_user = User.objects.create_user(
            username="other_user",
            email="other@example.com",
            password="password123"
        )

        self.category = Category.objects.create(
            user=self.user,
            name="Food"
        )

        self.income = Transaction.objects.create(
            user=self.user,
            title="Salary",
            amount=Decimal("3000.00"),
            type=Transaction.TransactionType.INCOME,
            category=self.category,
            date="2026-07-27"
        )

        self.expense = Transaction.objects.create(
            user=self.user,
            title="Groceries",
            amount=Decimal("500.00"),
            type=Transaction.TransactionType.EXPENSE,
            category=self.category,
            date="2026-07-26"
        )

        Transaction.objects.create(
            user=self.other_user,
            title="Other Salary",
            amount=Decimal("10000.00"),
            type=Transaction.TransactionType.INCOME,
            category=self.category,
            date="2026-07-25"
        )

    def test_total_income(self):
        service = DashboardService(
            user=self.user
        )

        result = service.get_total_income()

        self.assertEqual(
            result,
            Decimal("3000.00"),
        )

    def test_total_expense(self):
        service = DashboardService(
            user=self.user
        )

        result = service.get_total_expense()

        self.assertEqual(
            result,
            Decimal("500")
        )

    def test_balance(self):
        service = DashboardService(
            user=self.user
        )

        result = service.get_balance()

        self.assertEqual(
            result,
            Decimal("2500.00")
        )

    def test_transactions_count(self):
        service = DashboardService(
            user=self.user
        )

        result = service.get_transactions_count()

        self.assertEqual(
            result,
            2
        )

    def test_user_data_is_isolated(self):
        service = DashboardService(
            user=self.user
        )

        self.assertEqual(
            service.get_total_income(),
            Decimal("3000.00")
        )