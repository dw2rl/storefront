from django.shortcuts import render
from django.db.models import F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Order, Customer


def say_hello(request):
    queryset = Customer.objects.annotate(new_id=F('id'))
    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
