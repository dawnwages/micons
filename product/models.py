# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from django.db import models
from django.utils import timezone
from django.db.models import ProtectedError

# Create your models here.
#Django Foreign Key Models

class Processor(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Os(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Memory(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Hd(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Display(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Ss(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Color(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Brand(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title





#Product Models
class ProductIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    
    ]
    
class ProductPage(Page):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    article_num = models.CharField(max_length=20)
    #BrandSegment
    CON = 'Consumer'
    COM = 'Commercial'
    busigroup = (
        (CON, 'Consumer'),
        (COM, 'Commercial'),
        )
    busigroup_choice = models.CharField(
        max_length=200,
        choices=busigroup,
        default=CON,
        )
    #Brand
    brandtype = models.ForeignKey('product.Brand', on_delete=models.PROTECT)
    Live = 'Live'
    CS = 'Coming Soon'
    EOL = 'End of Life'
    status_type = (
        (Live, 'Live'),
        (CS, 'Coming Soon'),
        (EOL, 'End of Life'),
        )
    status_choice = models.CharField(
        max_length=200,
        choices=status_type,
        default= Live,
        )
    #Device Type
    LT = 'Laptops'
    DT = 'Desktops'
    DTA = 'Desktops - AIO'
    ACC = 'Accessories'
    WS = 'WorkStations'
    TB = 'Tablets'
    SD = 'Smart Devices'
    SSN = 'Servers Storage and Networking'
    device_type = (
        (LT, 'Laptops'),
        (DT, 'Desktops'),
        (DTA, 'Desktops All-In-Ones'),
        (ACC, 'Accessories'),
        (WS, 'Workstations'),
        (TB, 'Tablets'),
        (SD, 'Smart Devices'),
        (SSN, 'Servers, Storage and Networking'),
        )
    device_choice = models.CharField(
        max_length=200,
        choices=device_type,
        default=LT,
        )
    hybrislink = models.TextField()
    halo = models.BooleanField(default=False)
    touch = models.BooleanField(default=False)
    conv = models.BooleanField(default=False)
    launch_notes = RichTextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    live_date = models.DateTimeField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('article_num'),
        FieldPanel('busigroup_choice'),
        FieldPanel('brandtype'),
        FieldPanel('status_choice'),
        FieldPanel('device_choice'),
        FieldPanel('hybrislink'),
        FieldPanel('halo'),
        FieldPanel('touch'),
        FieldPanel('conv'),
        FieldPanel('created_date'),
        FieldPanel('live_date'),
        FieldPanel('launch_notes', classname="full"),
    ]
    
