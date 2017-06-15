from django.shortcuts import render, get_object_or_404
from .models import Category, Product,Client
from django.utils import timezone

# Create your views here.
def index(request):
    category = Category.objects.select_related()
    products = Product.objects.select_related()
    return render(request,'ganagroapp/index.html', {'category' : category, 'products' : products} )

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category = Category.objects.select_related()
    return render(request,'ganagroapp/product_detail.html',{'category' : category, 'product': product} )

def product_category(request, pk):
    products =Product.objects.filter(category=pk).select_related
    category = Category.objects.select_related()
    return render(request,'ganagroapp/product_category.html',{'category' : category, 'products': products})
