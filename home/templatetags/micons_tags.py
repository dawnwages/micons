from django import template
from product.models import *

register = template.Library()



# skus snippets
@register.inclusion_tag('home/tags/SKU.html', takes_context=True)
def skus(context):
    return {
        'skus': Sku.objects.all(),
        'request': context['request'],
    }
