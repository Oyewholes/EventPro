"""EventBrite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.HomePage.as_view(), name='home'),
    re_path(r'^test/$', views.TestPage.as_view(), name='test'),
    re_path(r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
    re_path(r'^appreciate/$', views.AppreciationPage.as_view(), name='appreciate'),
    re_path(r'^find/$', views.FindPage.as_view(), name = 'find'),
    re_path(r'^help/$', views.HelpPage.as_view(), name = 'help'),
    re_path(r'^thanksreg/$', views.ThanksRegistration.as_view(), name='thanksreg'),
    re_path(r'^accounts/', include('accounts.urls', namespace='accounts')),
    re_path(r'^accounts', include('django.contrib.auth.urls')),
    re_path(r'CreateEvent/', include("CreateEvent.urls", namespace="CreateEvent")),
    re_path(r'EventFinder/', include("EventFinder.urls", namespace="EventFinder"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
