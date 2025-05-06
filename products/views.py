from django.http import JsonResponse
from django.shortcuts import render
from products.models import Product
from products.serilizers import ProductSerializer


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

def api_products_list(request):
    if request.method=='GET':
        products = Product.objects.all()
        s = ProductSerializer(products, many=True)
        return JsonResponse(s.data, safe=False)


# response = http.get(mysite/api/products)
# response.data[]