from django.core import validators
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(
        label="User name field", 
        max_length=100, 
        required=True, 
        initial="John Doe", 
        validators=[validators.MaxLengthValidator(10, "Name is too long")])
    password = forms.CharField(
        label="Password field", 
        max_length=100, 
        required=True, 
        widget=forms.PasswordInput, 
        help_text="Enter password here",)
    about = forms.CharField(label="About", max_length=10000, required=False, widget=forms.Textarea(attrs={}))
