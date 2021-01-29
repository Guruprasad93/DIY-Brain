from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import LoginForm
from signupmanager.forms import SignUpForm
from .utils import verify_credentials, add_session
from django.shortcuts import render


# Create your views here.
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        signup_form_class = SignUpForm
        context = {
            'login_form_class': form_class,
            'signup_form_class': signup_form_class,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        signup_form_class = SignUpForm

        if form.is_valid():
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']

            if verify_credentials(email_address, password):
                add_session(request, email_address)
                return HttpResponseRedirect("/homepage")
            else:
                context = {
                    'login_form_class': form_class,
                    'signup_form_class': signup_form_class,
                    'login_invalid': True,
                    'message': 'Please check the username and password'
                }
                return render(request, self.template_name, context=context)
        else:
            context = {
                'login_form_class': form_class,
                'signup_form_class': signup_form_class,
                'login_invalid': True,
                'message': 'Invalid form entry'
            }
            return render(request, self.template_name, context=context)
