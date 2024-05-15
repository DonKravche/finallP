from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import CustomUser here


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100, required=True)
    personal_number = forms.CharField(max_length=20, required=True)
    birth_date = forms.DateField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'full_name', 'personal_number', 'birth_date', 'password1', 'password2')

    # ... (the rest of the RegistrationForm code)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
