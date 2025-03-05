from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='Username')
    email = forms.EmailField()
    