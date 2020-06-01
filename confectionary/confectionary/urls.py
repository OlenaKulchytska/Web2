"""confectionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from cupcakes import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('dishes/',  views.list_dishes),
    re_path('dishes/(?P<code>\w+)/$', views.dish_details),
    path('index/', views.client),
    path('index/menu.html/', views.menu),
    path('index/login.html/', views.login),
    path('index/registration.html/', views.registration),
    path('calls/',  views.list_calls),
    re_path('calls/(?P<pk>\d+)/$', views.call_details),
    path('list.html/',  views.list),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
