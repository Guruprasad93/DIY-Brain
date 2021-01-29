from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import SignUpForm
from loginmanager.forms import LoginForm
from .utils import save_details, new_user
from loginmanager.utils import add_session


# Create your views here.
class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        login_form_class = LoginForm
        context = {
            'signup_form_class': form_class,
            'login_form_class': login_form_class
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        login_form_class = LoginForm

        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']

            if new_user(email_address):
                save_details(full_name, email_address, password)
                add_session(request, email_address)
                return HttpResponseRedirect("/homepage")
            else:
                context = {
                    'signup_form_class': form_class,
                    'login_form_class': login_form_class,
                    'signup_invalid': True,
                    'message': 'User already exists'
                }
                return render(request, self.template_name, context=context)
        else:
            context = {
                'signup_form_class': form_class,
                'login_form_class': login_form_class,
                'signup_invalid': True,
                'message': 'Invalid form entry'
            }
            return render(request, self.template_name, context=context)
