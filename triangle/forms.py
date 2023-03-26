from django import forms

from .models import Person


class Hypotenuse(forms.Form):
    base = forms.IntegerField(label="Length of the triangle's base", help_text='mm', min_value=1)
    altitude = forms.IntegerField(label="Length of the triangle's altitude", help_text='mm', min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
