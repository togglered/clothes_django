from django.shortcuts import render, get_object_or_404
import random

from .models import Product, Category, SubCategory


def index(request):
    all_products = []

    categories = Category.objects.all()

    for category in categories:
        subcategories = category.subcategories.all()
        for subcategory in subcategories:
            all_products.extend(subcategory.products.all())

    products = random.choices(all_products, k=3) if len(all_products) >= 3 else None

    return render(request,
                  'main/index/index.html',
                  {'products': products,
                   "categories": categories})


def subcategory(request, category_slug, subcategory_slug):
    sorted = request.GET.get('sorted')
    if not sorted:
        sorted = '-created'

    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)

    products = subcategory.products.filter(available=True).order_by(sorted)

    showed_products = 9
    current_page = int(request.GET.get('page', 1))
    try:
        current_page_products = products[(showed_products) * (current_page - 1):(showed_products) * current_page]
    except IndexError:
        current_page_products = products[(showed_products) * (current_page - 1):len(products) + 1]
    if len(products) / showed_products % 1 == 0:
        pages = range(1, len(products) // showed_products + 1)
    else:
        pages = range(1, len(products) // showed_products + 2)
    counter_start = showed_products * (current_page - 1)

    return render(request,
                  'main/category/index.html',
                  {'products': products,
                   'counter_start': counter_start,
                   'current_page': current_page,
                   'pages': pages})


def product_info(request, id):
    product = get_object_or_404(Product, id=id)
    sizes = product.sizes.all()

    if request.method == "GET":
        return render(request,
                    'main/product/info.html',
                    {'product': product,
                    'sizes': sizes})
