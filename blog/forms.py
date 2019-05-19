from django import forms

class contactForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class modifierEmail(forms.Form):
    email = forms.EmailField()


