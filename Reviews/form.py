from django.forms import ModelForm
from django import forms
from .models import Review
from django.contrib.auth.models import User

RATING_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]
class ReviewForm(ModelForm):
    rating = forms.IntegerField(
        widget=forms.RadioSelect(choices=RATING_CHOICES)
    )
    review_text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Review
        fields = ["review_id", "rating", "review_text", "review_date"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']