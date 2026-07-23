# from django.shortcuts import render
# from django.db.models import Sum, Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# from transactions.models import Transaction
# from decimal import Decimal
# from django.db.models.functions import TruncMonth
from .services import DashboardService
from .serializers import DashboardSerializer
from datetime import date

# Create your views here.
class   DashboardView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        date_after = request.query_params.get(
            "date_after"
        )

        date_before = request.query_params.get(
            "date_before"
        )

        service = DashboardService(
            request.user,
            date_after=date_after,
            date_before=date_before
        )
        
        data = service.get_dashboard()

        serializer = DashboardSerializer(data)
        return Response (
            # service.get_dashboard()
            serializer.data
        )
        # expense = (
        #     Transaction.objects.filter(
        #         user = request.user,
        #         type = Transaction.TransactionType.EXPENSE
        #     )
        #     .aggregate(total = Sum("amount"))["total"]
        #     or Decimal('0')
        # )

        # income =(
        #     Transaction.objects.filter(
        #         user = request.user,
        #         type = Transaction.TransactionType.INCOME
        #     )
        #     .aggregate(total = Sum("amount"))["total"]
        #     or Decimal('0')
        # )

        # balance = income - expense

        # transactions_count = (
        #     Transaction.objects.filter(
        #         user = request.user
        #     )
        #     .aggregate(total = Count("id"))["total"]
        # )
        
        # expenses_by_category = (
        #     Transaction.objects.filter(
        #         user = request.user,
        #         type = Transaction.TransactionType.EXPENSE
        #     )
        #     .values("category__name")
        #     .annotate(total = Sum("amount"))
        #     .order_by("-total")
        # )

        # incomes_by_category = (
        #     Transaction.objects.filter(
        #         user = request.user,
        #         type = Transaction.TransactionType.INCOME
        #     ).values("category__name")
        #     .annotate(total=Sum("amount"))
        #     .order_by("-total")
        # )

        # monthly_expenses = (
        #     Transaction.objects.filter(
        #         user = request.user,
        #         type = Transaction.TransactionType.EXPENSE
        #     )
        #     .annotate(month=TruncMonth("date"))
        #     .values("month")
        #     .annotate(total = Sum("amount"))
        #     .order_by("total")
        # )

        # monthly_incomes = (
        #     Transaction.objects.filter(
        #         user = request.user,
        #         type = Transaction.TransactionType.INCOME
        #     )
        #     .annotate(month=TruncMonth("date"))
        #     .values("month")
        #     .annotate(total = Sum("amount"))
        #     .order_by("total")
        # )

        # return Response({
        #     "total_income": income,
        #     "total_expense": expense,
        #     "balance": balance,
        #     "transactions_count": transactions_count,
        #     "expenses_by_category": expenses_by_category,
        #     "incomes_by_category": incomes_by_category,
        #     "monthly_expenses": monthly_expenses,
        #     "monthly_incomes": monthly_incomes
        # })
