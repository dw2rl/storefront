from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, Order


def say_hello(request):
    queryset = Order.objects.select_related(
        'customer').order_by('-placed_at').prefetch_related('orderitem_set__product')[:5]
    return render(request, 'hello.html', {'name': 'Mosh', 'orders': list(queryset)})
