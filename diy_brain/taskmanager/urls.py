from django.conf.urls import url
from .views import TaskView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  url("^$", csrf_exempt(TaskView.as_view()), name="taskmanagerview")
]
