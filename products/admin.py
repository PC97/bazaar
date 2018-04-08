# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from products.models import *

# Register your models here.
# class InventoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'publisher', 'description', 'pub_date', '__unicode__')


admin.site.register(Inventory)

#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'category')
#     prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product)


# class ProductDetailAdmin(admin.ModelAdmin):
#     list_display = ('product', 'attribute', 'value')


admin.site.register(ProductDetail)


# class ProductAttributeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')


admin.site.register(ProductAttribute)