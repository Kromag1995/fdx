"User creation form"
from django import forms

class UserCreationForm(forms.Form):
    "User creation form template"
    username = forms.CharField(label='Username', max_length=200)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    email = forms.EmailField()
    