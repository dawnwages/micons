# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailcore.fields import ( RichTextField, StreamField )
from wagtail.wagtailadmin.edit_handlers import ( FieldPanel, MultiFieldPanel, StreamFieldPanel )
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.db import models
from django.utils import timezone
from django.db.models import ProtectedError
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager


# Create your models here.
#Django Foreign Key Models

@register_snippet
class ProductTag(TaggedItemBase):
	content_object = models.CharField(max_length=50, db_index=True)
	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tags"

@register_snippet
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

    def __unicode__(self):
        return self.title

@register_snippet
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

    def __unicode__(self):
        return self.title

@register_snippet
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

    def __unicode__(self):
        return self.title

@register_snippet
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

    def __unicode__(self):
        return self.title

@register_snippet
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

    def __unicode__(self):
        return self.title

@register_snippet
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

    def __unicode__(self):
        return self.title

@register_snippet
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

    def __unicode__(self):
        return self.title

@register_snippet
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

    def __unicode__(self):
        return self.title

    #Adding the SKU Module - I'm going to keep it as models.
    #Models file because I don't need to have the Page functionality built in with django models. 
    #This also will be helpful to just edit the full list
    
@register_snippet
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
    
    """
    This is merging the TD tutorial and the wagtail bakery demo
    Each of the aspects are divided into discrete functions to make it easier to follow.
    """
    intro = RichTextField(
        help_text='Text to describe the index of the products',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Pretty Banner Image :)')
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('image'),
    ]
    
    #Can only have ProductPage children
    subpage_types = ['ProductPage']
    
    """ 
    This is the way that we render product list from TD's tutorial. 
    Comment out and use wagtail bakery demo
    
    def get_context(self, request):
    # Update context to include only published posts, 
    # in reverse chronological order
	    context = super(ProductIndexPage, self).get_context(request)
	    live_productpages = self.get_children().live()
	    context['productpages'] = live_productpages.order_by('-first_published_at')
	    return context
    """
    # Returns a queryset of ProductPage objects that are live, that are direct
    # descendants of this index page with most recent first
    def get_products(self):
        return ProductPage.objects.live().descendant_of(
            self).order_by('-first_published_at')


    # Allows child objects (e.g. BreadPage objects) to be accessible via the
    # template. We use this on the HomePage to display child items of featured
    # content
    def children(self):
        return self.get_children().specific().live()
	   
	   
 # Pagination for the index page. We use the `django.core.paginator` as any
    # standard Django app would, but the difference here being we have it as a
    # method on the model rather than within a view function
    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_products(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    # Returns the above to the get_context method that is used to populate the
    # template
    def get_context(self, request):
        context = super(ProductIndexPage, self).get_context(request)

        # ProductPage objects (get_products) are passed through pagination
        products = self.paginate(request, self.get_products())

        context['products'] = products

        return context


class ProductPage(Page):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    article_num = models.CharField(max_length=20)
    feature_image = models.ForeignKey('wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    thumbnail_image = models.ForeignKey('wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    short_desc = models.CharField(max_length=250, blank=True)
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
    tags = TaggableManager(through=ProductTag, blank=True)
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
        FieldPanel('tags'),
        FieldPanel('created_date'),
        FieldPanel('live_date'),
        FieldPanel('launch_notes', classname="full"),
        ImageChooserPanel('feature_image'),
        ImageChooserPanel('thumbnail_image'),
    ]
    

    
