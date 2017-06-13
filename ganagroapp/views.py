from django.shortcuts import render
from .models import Category, Product,Client
from django.utils import timezone

# Create your views here.
def index(request):
    category = Category.objects.all()
    products = Product.objects.select_related()
    client = Client.objects.all()
    return render(request,'ganagroapp/index.html', {'category' : category, 'products' : products} )
