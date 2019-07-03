from django import forms

class contactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='email')
