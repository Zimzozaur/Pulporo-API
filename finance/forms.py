from datetime import date
from collections import OrderedDict
from django import forms
from .models import OneIO, ManagerIO


class BaseIOForm(forms.ModelForm):
    class Meta:
        fields = [
            'title',
            'value',
            'notes',
        ]
    title = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={
            'class': 'add-form-title',
            'placeholder': 'Title',
        })
    )
    value = forms.DecimalField(
        min_value=0,
        max_digits=17,
        decimal_places=2,
        label=False,
        widget=forms.NumberInput(attrs={
            'class': 'add-form-value',
            'placeholder': 100.01
        })
    )
    notes = forms.CharField(
        label=False,
        required=False,
        widget=forms.Textarea({
            'class': 'add-form-notes',
            'placeholder': 'Place your notes here',
        })
    )


class ManagerIOForm(BaseIOForm):
    class Meta(BaseIOForm.Meta):
        model = ManagerIO
        fields = BaseIOForm.Meta.fields + [
            'active',
            'interval_start',
            'interval_end',
            'interval',
        ]


class OneIOForm(BaseIOForm):
    class Meta(BaseIOForm.Meta):
        fields = BaseIOForm.Meta.fields + ['is_outcome', 'date', 'prediction']
        model = OneIO

    date = forms.DateField(
        label=False,
        initial=date.today(),
        widget=forms.DateInput(attrs={
            'class': 'add-form-date',
            'type': 'date',
        })
    )

    prediction = forms.BooleanField(
        label=False,
        initial=True,
        help_text='Prediction',
        widget=forms.CheckboxInput(attrs={
            'class': 'add-form-prediction'
        })
    )

    is_outcome = forms.BooleanField(
        label=False,
        initial=True,
        help_text='Outcome',
        widget=forms.CheckboxInput(attrs={
            'class': 'add-form-prediction'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reorder fields
        field_order = ['title', 'is_outcome', 'value', 'date', 'prediction', 'notes']
        self.fields = OrderedDict((key, self.fields[key]) for key in field_order)


