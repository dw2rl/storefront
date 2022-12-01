from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Order


def say_hello(request):
    result = Product.objects.aggregate(Count('id'), Min('unit_price'))
    return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
