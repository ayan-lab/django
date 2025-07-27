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
    
    return render(request, 'index.html')