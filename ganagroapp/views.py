from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product,Client,Image
from django.utils import timezone
from .forms import *
from django.template import RequestContext, loader, Context, Template
from django.core.urlresolvers import reverse
from django.http import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    images = Image.objects.select_related()
    category = Category.objects.select_related()
    products = Product.objects.select_related()
    return render(request,'ganagroapp/index.html', {'category' : category, 'products' : products, 'images': images} )

def product_detail(request, pk):
    product = get_object_or_404(Image, product_id=pk)
    images = Image.objects.select_related()
    category = Category.objects.select_related()
    return render(request,'ganagroapp/product_detail.html',{'category' : category, 'product': product, 'images': images} )

def product_category(request, pk):
    images = Image.objects.select_related()
    products =Product.objects.filter(category=pk).select_related
    category = Category.objects.select_related()
    return render(request,'ganagroapp/product_category.html',{'category' : category, 'products' : products, 'images' : images})

@login_required
def profile(request, pk):
    images = Image.objects.select_related()
    #client = Client.objects.filter(user_id=pk).select_related()
    products = Product.objects.filter(client_id=pk).select_related
    category = Category.objects.select_related()
    return render(request,'ganagroapp/profile.html',{'category' : category, 'products' : products, 'images' : images})

def register_user(request):
	username = password = email = first_name = last_name=''
	if request.POST:
		user_form = UserCreateForm(request.POST)
		if user_form.is_valid():
			usuario = User(username=request.POST['username'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
			usuario.set_password(request.POST['password1'])
			usuario.save()
			return HttpResponseRedirect(reverse('ganagroapp:index'))
	else:
		user_form = UserCreateForm()

	dictionary = {
		'user_form': user_form,
		'page_title': 'Aplicacion - Register',
		'body_class': 'register',
	}
	return render(request, "new_user.html", dictionary,{'user_form' : user_form})
@login_required
def new_product(request):
    if request.method == "POST":
            form = ProductForm(request.POST)
            form2 = ProductImageForm(request.POST, request.FILES)
            if form.is_valid() and form2.is_valid():
                product = form.save(commit=False)
                image = form2.save(commit=False)
                product.Client = request.user
                product.client_id = request.user.pk
                product.created_date = timezone.now()
                product.save()
                image.product_id = product.pk
                image.save()
                message="Producto cargado exitosamente"
                return redirect('ganagroapp:product_detail', pk=product.pk)
    else:
        form = ProductForm()
        form2 = ProductImageForm()
    return render(request, 'ganagroapp/new_product.html',{'form': form, 'form2':form2 })
@login_required
def edit_product(request, pk, pk1):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('ganagroapp:profile',pk=pk1)
    else:
        form = ProductForm(instance=product)
    return render(request, 'ganagroapp/new_product.html',{'form': form})
