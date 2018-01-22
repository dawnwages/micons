# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from taggit.models import Tag

from django.contrib.auth.models import User
from product.models import *

#from product.filters import ProductFilter

# Create your views here.




class ProductListView(ListView):
    template_name = 'product/product_list.html'
    
    def get_queryset(self):
        self.producttags = get_object_or_404(ProductPage, name=self.args[0])
        return ProductTag.objects.filter(publisher=self.productpage)
    #product_list = ProductPage.objects.all()
    #product_filter = ProductFilter(request.GET, queryset=product_list)
    #return render(request, 'search/product_list.html', {'filter': product_filter})
