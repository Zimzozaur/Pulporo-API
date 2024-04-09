from django.forms import ModelForm, ValidationError, DateInput, BooleanField
from django.contrib.auth.models import User
from .models import OneIO


class UpdateIOForm(ModelForm):
    class Meta:
        model = OneIO
        fields = ['title', 'value', 'is_outcome', 'date', 'prediction', 'cash_tag_id', 'company_id', 'notes']
        is_outcome = BooleanField()
        date = DateInput()
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cash_tag_id'].required = False
        self.fields['company_id'].required = False
        self.fields['notes'].required = False
        self.fields['is_outcome'].required = False
        self.fields['is_outcome'].initial = True
        self.fields['is_outcome'].label = 'Outcome'

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



