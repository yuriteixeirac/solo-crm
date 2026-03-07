from django import forms
from crm.models import Interaction


class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = '__all__'
