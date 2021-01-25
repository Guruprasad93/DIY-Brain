from django import forms


class LoginForm(forms.Form):
    email_address = forms.EmailField(label='Email Address', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
