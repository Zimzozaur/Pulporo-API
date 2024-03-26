from django.forms import ModelForm
from .models import OneIO


class UpdateIOForm(ModelForm):
    class Meta:
        model = OneIO
        fields = ['title', 'value', 'date', 'future', 'cash_tag', 'company', 'notes']

    def clean(self):
        cleaned = super().clean()
        value = cleaned.get('value')
        title = cleaned.get('title')
        if value < 0:
            raise ValueError('Value mast be equal or greater than 0')
        if not title and len(title) == 0:
            raise ValueError('Title has to be at list 1 non-space character')

        return cleaned
