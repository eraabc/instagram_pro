from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин или Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

