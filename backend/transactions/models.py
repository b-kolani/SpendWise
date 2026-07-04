from django.conf import settings
from django.db import models

# Create your models here.
class   Transaction(models.Model):
    
    class   TransactionType(models.TextChoices):
        INCOME = 'INCOME', 'Income'
        EXPENSE = 'EXPENSE', 'Expense'
    
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

    type = models.CharField(
        max_length=7,
        choices=TransactionType.choices
    )

    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.PROTECT,
        related_name='transactions'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class   Meta:
        ordering = ['-date', '-created_at']
        
    def __str__(self):
        return f"{self.title} ({self.amount})"