# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
from products.models import Product
from . import views


urlpatterns = [
    #url(r'^shit',)
    #'django.views.generic.list_detail',
    #url(r'^product/$', 'object_list', {'queryset': Product.objects.all()}, name='product_list'),
    url(r'^product/$', views.IndexView.as_view(), name='product_list'),
    url(r'^product/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='product_detail'),
    #url(r'^product/(?P<slug>[-\w]+)/$', 'object_detail',{'queryset': Product.objects.all()},name='product_detail')
    ]
