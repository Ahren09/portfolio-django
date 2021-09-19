#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:blog_id>/', views.detail, name='deta'),
]
