from django import forms


class Hypotenuse(forms.Form):
    base = forms.IntegerField(label="Length of the triangle's base", help_text='mm', min_value=1)
    altitude = forms.IntegerField(label="Length of the triangle's altitude", help_text='mm', min_value=1)
