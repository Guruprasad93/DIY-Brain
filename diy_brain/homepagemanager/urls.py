from django.conf.urls import url
from .views import HomePageView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  url("^$", csrf_exempt(HomePageView.as_view()), name="homepagemanagerview")
]
