"""diy_brain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from loginmanager.views import LoginView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', csrf_exempt(LoginView.as_view()), name="home"),
    url(r'^login/', include("loginmanager.urls")),
    url(r'^signup/', include("signupmanager.urls")),
    url(r'^homepage/', include("homepagemanager.urls")),
    url(r'^task/$', include("taskmanager.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
