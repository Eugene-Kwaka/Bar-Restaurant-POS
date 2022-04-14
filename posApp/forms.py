
from django import forms
from .models import *


class SalesSearchForm(forms.ModelForm):
    # This helps us choose which search field to fill without necessarily filling all required fields
    #category = forms.CharField(required=False)
    product_id = forms.CharField(required=False)
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)

    class Meta:
        model = salesItems
        fields = ['item_name', 'start_date', 'end_date']