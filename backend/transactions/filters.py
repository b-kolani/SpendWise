import django_filters

from .models import Transaction

class   TransactionFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        choices=Transaction.TransactionType.choices
    )

    category = django_filters.NumberFilter()
    
    amount__min = django_filters.NumberFilter(
        field_name="amount",
        lookup_expr="gte"
    )

    amount__max = django_filters.NumberFilter(
        field_name="amount",
        lookup_expr="lte"
    )

    class   Meta:
        model = Transaction
        fields = []
