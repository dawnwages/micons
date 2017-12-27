from django import template
from home.models import *

register = template.Library()



# skus snippets
@register.inclusion_tag('home/tags/nav.html', takes_context=True)
def logos(context):
    return {
        'logos': Logo.objects.all(),
        'request': context['request'],
    }