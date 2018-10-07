#!/usr/bin/env python3

"""driving_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    path('news/', views.news, name='news'),
    re_path('news/post/(?P<post>[0-9]+)/$', views.news_post, name='post'),
    path('teachers/', views.teachers, name='teachers'),
    path('classes/', views.classes, name='classes'),
    path('classes/<branch>/', views.form_record, name='form'),
    path('add_order/', views.add_order, name='add_order'),
    path('confidential/', views.get_confidential, name='confidential'),

]
