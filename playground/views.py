from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product, Order, OrderItem
from tags.models import TaggedItem
from django.db import transaction

# Create your views here.
# request -> response
# request handler

def say_hello(request):
    # query_set = Product.objects.values('title','orderitem__product_id').order_by('title')
    
    orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    queryset = TaggedItem.objects.get_tags_for( Product, 1)
   
    
    return render(request, 'index.html', {'name': "mysql", 'orders': list(orders), 'tags':list(queryset)})