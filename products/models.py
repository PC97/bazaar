# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# from django.db.models.signals import pre_save
# from django.utils.text import slugify
# from django.utils import unique_slug_generator


# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    description =  models.TextField(blank='TRUE')

    def __unicode__(self):
        return self.name


class Product(models.Model):
    '''
    The ``Product`` model represents a particular item in a catalog of
    products. It contains information about the product for sale,
    which is common to all items in the catalog. These include, for
    example, the item's price, manufacturer, an image or photo, a
    description, etc.
    '''
    categoryID = models.ForeignKey('Inventory', related_name='products')
    name = models.CharField(max_length=350)
    slug = models.SlugField(max_length=150,unique=True)
    description = models.TextField(blank='True')
    manufacturer = models.CharField(max_length=50, blank='True')
    photo = models.ImageField(upload_to='static/img/product_photo', blank='True')
    #price_in_rupees = models.DecimalField(max_digits='8',decimal_places='2')

    def __unicode__(self):
        return 'self.name'

    #def get_price(self):
     #   return self.price_in_rupees

    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug':self.slug})


class ProductDetail(models.Model):
    '''
    The ``ProductDetail`` model represents information unique to a
    specific product. This is a generic design that can be used to
    extend the information contained in the ``Product`` model with
    specific, extra details.
    '''
    product = models.ForeignKey('Product', related_name='details')
    attribute = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.product, self.attribute)


class ProductAttribute(models.Model):
    '''
    The ``ProductAttribute`` model represents a class of feature found
    across a set of products. It does not store any data values
    related to the attribute, but only describes what kind of a
    product feature we are trying to capture.

    Possible attributes include things like materials, colors, sizes,
    and many, many more.
    '''
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % self.name

    # def create_slug(instance, new_slug=None):
    #     slug = slugify(instance.title)
    #     if new_slug is not None:
    #         slug = new_slug
    #     qs = Post.objects.filter(slug=slug).order_by("-id")
    #     exists = qs.exists()
    #     if exists:
    #         new_slug = "%s-%s" % (slug, qs.first().id)
    #         return create_slug(instance, new_slug=new_slug)
    #     return slug
    #
    # '''
    # unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
    # '''
    #
    #
    # def pre_save_post_receiver(sender, instance, *args, **kwargs):
    #     if not instance.slug:
    #         # instance.slug = create_slug(instance)
    #         instance.slug = unique_slug_generator(instance)
    #
    # pre_save.connect(pre_save_post_receiver, sender=Post)
    #
