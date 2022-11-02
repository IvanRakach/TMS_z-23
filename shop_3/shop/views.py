from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def index(request):
    return render(request, 'shop/base.html',
                  {'title': 'Главная страница"'})

def product_list(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/pr_list.html',
                  {'title': 'PR"'})

#
def product_detail(request):
    return render(request, 'shop/detail.html',
                  {'title': 'detail"'})

# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'shop/pr_list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products})


# def product_detail(request, pk, slug):
#     product = get_object_or_404(Product,
#                                 # pk=pk,
#                                 # slug=slug,
#                                 available=True)
#     return render(request,
#                   'shop/detail.html',
#                   {'product': product})
