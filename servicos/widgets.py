from django import forms
from django.utils import timezone

class CurrentDateWidget(forms.DateInput):
    def __init__(self, attrs=None):
        attrs = {'type': 'date'}
        super().__init__(attrs)

    def format_value(self, value):
        if value is None:
            value = timezone.now().strftime('%Y-%m-%d')
        return super().format_value(value)
