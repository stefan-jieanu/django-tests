from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from products.models import Product


# Create your views here.
def homepage(request):
    return render(
        request,
        'index.html'
    )

def products_page(request):
    products = Product.objects.all()

    return render(
        request,
        'products.html',
        context={
            'products': products
        }
    )