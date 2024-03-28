from django.forms import ModelForm, ValidationError
from .models import OneIO


class UpdateIOForm(ModelForm):
    class Meta:
        model = OneIO
        fields = ['title', 'value', 'date', 'future', 'cash_tag', 'company', 'notes']

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

