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

    #Adding the SKU Module - I'm going to keep it as models.
    #Models file because I don't need to have the Page functionality built in with django models. 
    #This also will be helpful to just edit the full list
    
class Sku(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=20)
    article = models.ForeignKey('product.ProductPage', on_delete=models.PROTECT) 
    friendly_name = models.CharField(max_length=200)
	#Country
    US = 'United States'
    CA = 'Canada'
    COUNTRY_TYPE = (
        (US, 'US'),
        (CA, 'CA'),
    )
    country_choice = models.CharField(
        max_length=15,
        choices=COUNTRY_TYPE,
        default=US,
        )
    #SKU STATUS
    Live = 'Live'
    NotLive = 'Not Live'
    BLOCKED = 'Blocked'
    TEMPUNAV = 'Temporarily Unavailable'
    STATUS_TYPE = (
        (Live, 'Live'),
        (NotLive, 'Not Live/Removed From Site'),
        (BLOCKED, 'Blocked'),
        (TEMPUNAV, 'Temporarily Unavailable'),
        )
    status_choices = models.CharField(
        max_length=200,
        choices=STATUS_TYPE,
        default=Live,
        )
    #Model Type
    MTM = 'Made to Manufacture'
    CTO = 'Configurable to Order'
    SKU_Type = (
        (MTM, 'Made to Manufacture'), 
        (CTO, 'Configurable to Order')
        )
    type_choices = models.CharField(
        max_length=200,
        choices=SKU_Type,
        default= MTM,
        )
    sku_link = models.TextField(default='NULL')
    processor_choice = models.ForeignKey('product.processor', on_delete=models.PROTECT)
    os_choice = models.ForeignKey('product.os', on_delete=models.PROTECT)
    memory_choice = models.ForeignKey('product.memory', on_delete=models.PROTECT)
    hd_choice = models.ForeignKey('product.hd', on_delete=models.PROTECT)
    display_choice = models.ForeignKey('product.display', on_delete=models.PROTECT)
    ss_choice = models.ForeignKey('product.ss', on_delete=models.PROTECT)
    color_choice = models.ForeignKey('product.color', on_delete=models.PROTECT)
    #Price Choices
    TierOne = '1'
    TierTwo = '2'
    TierThree = '3'
    TierFour = '4'
    Price_Tier = (
        (TierOne, 'Above $3,000'),
        (TierTwo, 'Between $1,000 - $2999.99'),
        (TierThree, 'Between $500 - $999.99'),
        (TierFour, 'Between $100 - $499.99'),
        )
    price_choice = models.CharField(
        max_length=15,
        choices=Price_Tier,
        default=TierThree,
        )
    #Dates
    created_date = models.DateTimeField(
        default=timezone.now)
    live_date = models.DateTimeField(
        blank=True, null=True)
    def publish(self):
        self.created_date = timezone.now()
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
    

    
