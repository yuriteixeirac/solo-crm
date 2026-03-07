from django import forms
from crm.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
