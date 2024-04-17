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
            'class': 'text-xl px-4 py-2 rounded-2xl',
            'placeholder': 'Title',
        })
    )
    value = forms.DecimalField(
        min_value=0,
        max_digits=17,
        decimal_places=2,
        label=False,
        widget=forms.NumberInput(attrs={
            'class': 'text-xl px-4 py-2 rounded-2xl',
            'placeholder': 100.01
        })
    )
    notes = forms.CharField(
        label=False,
        required=False,
        widget=forms.Textarea({
            'class': 'text-xl px-4 py-2 rounded-2xl h-16 min-h-16 max-h-32',
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
        fields = BaseIOForm.Meta.fields + ['date', 'prediction']
        model = OneIO

    date = forms.DateField(
        label=False,
        initial=date.today(),
        widget=forms.DateInput(attrs={
            'class': 'text-xl px-4 py-2 rounded-2xl',
            'type': 'date',
        })
    )

    prediction = forms.BooleanField(
        label=False,
        initial=True,
        help_text='Prediction',
        widget=forms.CheckboxInput(attrs={
            'class': 'rounded w-5 h-5'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reorder fields
        field_order = ['title', 'value', 'date', 'prediction', 'notes']
        self.fields = OrderedDict((key, self.fields[key]) for key in field_order)


