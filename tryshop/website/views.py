from django.shortcuts import render, redirect, get_object_or_404

from tryshop.product.models import Product

def index(request):
    product_list = Product.objects.all()
    lists = [1,2,3,4,5]
    context = {
        'lists': lists
    }
    return render(request, 'index.html', context)
