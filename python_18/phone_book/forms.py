from django import forms

class AddContact(forms.Form):
    name = forms.CharField(label="Name")
    lastname = forms.CharField(label="Lastname")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Tel")
    about = forms.CharField(label="About")
