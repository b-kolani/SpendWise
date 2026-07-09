import django_filters

from .models import Transaction

class   TransactionFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        choices=Transaction.TransactionType.choices
    )

    category = django_filters.NumberFilter()
    
    amount_min = django_filters.NumberFilter(
        field_name="amount",
        lookup_expr="gte"
    )

    amount_max = django_filters.NumberFilter(
        field_name="amount",
        lookup_expr="lte"
    )

    date = django_filters.DateFilter()

    date_before = django_filters.DateFilter(
        field_name="date",
        lookup_expr="lte"
    )

    date_after = django_filters.DateFilter(
        field_name="date",
        lookup_expr="gte"
    )
    
    class   Meta:
        model = Transaction
        fields = []
