from django import forms
from film.models import Filmview

class movieform(forms.ModelForm):
    class Meta:
        model=Filmview
        fields='__all__'