from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .forms import AddToCartForm, CreateOrderForm
from main.models import OrderItem, Order, ProductSize
from .cart import Cart


@require_POST
def add(request, id):
    size = get_object_or_404(ProductSize, id=id)
    form = AddToCartForm(size.product, request.POST)
    if form.is_valid():
        size = form.cleaned_data['size']
        cart = Cart(request)
        cart.add(size)
    return redirect('main:product_info',
                    id = size.product.id)


@require_POST
def remove(request, id):
    size = get_object_or_404(ProductSize, id=id)
    cart = Cart(request)
    cart.remove(size)
    return redirect('cart:cart_detail')


@require_POST
def clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')


@require_POST
def pay(request):
    cart = Cart(request)
    form = CreateOrderForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        for size_id, dict in cart.cart.items():
            size = get_object_or_404(ProductSize, id=int(size_id))
            if size.stock < dict['quantity']:
                return redirect('cart:cart_detail')
        
        order = Order.objects.create(
            name = cd['name'],
            surname = cd['surname'],
            city = cd['city'],
            street = cd['street'],
            house = cd['house'],
            flat = cd['flat'],
            email = cd['email']
        )
        for size_id, dict in cart.cart.items():
            size = get_object_or_404(ProductSize, id=int(size_id))
            OrderItem.objects.create(order=order, product_size=size, quantity=dict['quantity'])
    return redirect('cart:cart_detail')


@require_POST
def create_order(request):
    cart = Cart(request)
    cart_sum = 0
    for size_id, dict in cart.cart.items():
        size = get_object_or_404(ProductSize, id=int(size_id))
        for _ in range(int(dict['quantity'])):
            cart_sum += size.product.price

    return render(request,
                  'cart/create-order.html',
                  {'cart_sum': cart_sum})
    


def cart_detail(request):
    cart = Cart(request)
    sizes = []
    cart_sum = 0
    for size_id, dict in cart.cart.items():
        size = get_object_or_404(ProductSize, id=int(size_id))
        for _ in range(int(dict['quantity'])):
            sizes.append(size)
            cart_sum += size.product.price
        
    return render(request,
                  'cart/detail.html',
                  {'cart': sizes,
                   'cart_sum': cart_sum})
