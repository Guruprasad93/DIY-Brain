from django import forms

class SignUpForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    email_address = forms.EmailField(label='Email Address', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
