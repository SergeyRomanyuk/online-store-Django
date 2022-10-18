from django.shortcuts import render, get_object_or_404
from .models import Deliv
from .models import Contact
from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'web/index.html')
def delivery(request):
    text=Deliv.objects.all()
    context1 = {
        'dv': text,
    }
    return render(request, 'web/delivery.html', context1)

def contact(request):
    text2 = Contact.objects.all()
    context2 = {
        'cont': text2,
    }
    return render(request, 'web/contact.html', context2)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'web/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'web/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

