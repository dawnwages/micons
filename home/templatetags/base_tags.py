from django import template
from home.models import *

register = template.Library()



#tools snippet
@register.inclusion_tag('home/tags/tools.html', takes_context=True)
def tools(context):
    return {
        'tools': Tools.objects.all(),
        'request': context['request'],
    }