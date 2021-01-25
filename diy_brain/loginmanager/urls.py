from django.conf.urls import url
from .views import LoginView
from .utils import remove_session
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  url("^$", csrf_exempt(LoginView.as_view()), name="loginview"),
  url("^logout$", remove_session, name="logoutview")
]
