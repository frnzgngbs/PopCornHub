from django import forms
from .models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']