import django_filters
from django_filters import DateTimeFromToRangeFilter, CharFilter

from .models import Sales


class SalesFilter(django_filters.FilterSet):
    code = CharFilter(field_name = 'code', lookup_expr="icontains")
    date_added = DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(
        attrs={'type': 'date'}
    )
    )
    # status = ChoiceFilter(choices=STATUS)
    # category = ChoiceFilter(choices=CATEGORY)

    class Meta:
        model = Sales
        fields = ['code', 'date_added']