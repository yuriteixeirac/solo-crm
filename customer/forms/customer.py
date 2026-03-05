from django import forms
from django.core.exceptions import ValidationError
from customer.models import Customer
from customer.validators import NumberValidator


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    
    def clean(self):
        cleaned_data = super().clean()

        number = cleaned_data.get('number')

        if number and not NumberValidator.validate(number):
            self.add_error('number', ValidationError('Phone is not valid.'))
        
        return cleaned_data
