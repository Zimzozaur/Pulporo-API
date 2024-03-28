from django.forms import ModelForm, ValidationError, DateInput
from django.contrib.auth.models import User
from .models import OneIO, Currency



class UpdateIOForm(ModelForm):
    class Meta:
        model = OneIO
        fields = ['title', 'value', 'date', 'future', 'cash_tag', 'company', 'notes']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})  # Use DateInput widget for date field
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cash_tag'].required = False
        self.fields['company'].required = False
        self.fields['notes'].required = False

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 0:
            raise ValidationError('Value mast be equal or greater than 0')
        return value

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title and len(title) == 0 or len(title) == 51:
            raise ValidationError('Title has to be between 1 and 50 charts')
        return title

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.owner = User.objects.get(pk=1)
        instance.currency = Currency.objects.get(pk=1)
        instance.save()
        return instance