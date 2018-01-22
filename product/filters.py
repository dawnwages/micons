from django.contrib.auth.models import User
from product.models import *
import django_filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = ProductPage
        fields = ['brandtype', 'tags',]