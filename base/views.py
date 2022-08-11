from itertools import product
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import json
from .models import Product, Order

# Create your views here.

def store(request):
    products = Product.objects.all()
    return render(request, 'base/store.html', {'products': products})


def checkout(request, pk):
    product = Product.objects.get(id=pk)
    
    return render(request, 'base/checkout.html', {'product':product})


def paymentComplete(request):
    body = json.loads(request.body)
    product = Product.objects.get(id=body['productId'])
    Order.objects.create(
        product=product
    )
    return JsonResponse("Payment Completed", safe=False)

