from django.db import models
    
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet

from django.utils import timezone
    
class HomePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    
@register_snippet
class Tools(models.Model):
    title =  models.TextField(
        help_text='Name of Resource',
        max_length = 255)
    icon = models.ForeignKey(
        'wagtailimages.Image',
        default='https://image.flaticon.com/icons/svg/25/25284.svg',
        blank=True,
        related_name='+',
        help_text='icon for your link.'
    )
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    link = models.URLField(
        max_length = 200,
        help_text = 'url',
        blank=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    
        