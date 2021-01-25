from django.conf.urls import url
from .views import SignUpView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  url("^$", csrf_exempt(SignUpView.as_view()), name="signupview")
]
