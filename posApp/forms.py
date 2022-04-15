from django import forms
from .models import *
from dataclasses import fields
from django.forms import widgets



class DateInput(forms.DateInput):
    input_type = 'date'

class SalesSearchForm(forms.ModelForm):
    # This helps us choose which search field to fill without necessarily filling all required fields
    #category = forms.CharField(required=False)
    code = forms.CharField(required=False)
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)

    class Meta:
        model =Sales
        widgets = {'start_date':DateInput(), 'end_date':DateInput()}
        fields = ['code', 'start_date', 'end_date']