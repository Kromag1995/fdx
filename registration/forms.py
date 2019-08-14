"User creation form"
from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.Form):
    "User creation form template"
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_conf = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    email = forms.EmailField()
    def clean(self):
        cleaned_data = super().clean()
        password_1 = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_conf')
        if password_1 != password_2:
            raise forms.ValidationError(("The passwords doenst match"), code='passwords')
        username = cleaned_data.get('username')
        try:
            if User.objects.get(username=username):
                raise forms.ValidationError("The username is taken", code='username')
        except:
            pass
        email = cleaned_data.get('email')
        try:
            if User.objects.get(email=email):
                raise forms.ValidationError("The email is alredy register, you\
         forgot your password?", code='email')
        except:
            pass
