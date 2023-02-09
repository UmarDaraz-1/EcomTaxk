from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
#from . import Cart
from .models import *
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from .forms import SearchForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')


def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def detail_product(request, item_id):
    product = Product.objects.get(id=item_id)
    if product:
        context = {
            "product_name": product.name,
            "product_description": product.description,
            "product_price": product.price,
            "product_image": product.image,
        }
        return render(request, "detail_product.html", context)


def search(request):
    form = SearchForm(request.GET)
    products = Product.objects.all()
    
    if form.is_valid():
        name = form.cleaned_data.get('name')
        category = form.cleaned_data.get('category')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if name:
            products = products.filter(name__icontains=name)
        if category:
            products = products.filter(category=category)
        if price_min:
            products = products.filter(price__gte=price_min)
        if price_max:
            products = products.filter(price__lte=price_max)

    return render(request, 'search.html', {'form': form, 'products': products})

'''def search(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'search.html', {"results":results})

    return render(request, 'search.html')
'''
'''
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_amount = 0
    for item in cart_items:
        total_amount += item.quantity * item.product.price

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'checkout.html', context)

'''


def checkout(request):
    session = Session.objects.get_or_create(session_key=request.session.session_key,
    defaults={'expire_date': datetime.now()})
    cart = session.get('cart', [])
    cart_items = []
    for item in cart:
        product = Product.objects.get(id=item['product_id'])
        cart_item = {
            'product': product,
            'quantity': item['quantity'],
        }
        cart_items.append(cart_item)

    # Calculate the total amount of the bill
    total_amount = 0
    for item in cart_items:
        total_amount += item['quantity'] * item['product'].price

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'checkout.html', context)







'''def checkout(request):
    # Get the cart items for the current session
    expire_date = datetime.now()
    session = Session.objects.get_or_create(
        session_key=request.session.session_key,
        defaults={'expire_date': expire_date}
    )
    cart_items = []
    for item in session.get('cart', []):
        product = Product.objects.get(id=item['product_id'])
        cart_item = {
            'product': product,
            'quantity': item['quantity'],
        }
        cart_items.append(cart_item)

    # Calculate the total amount of the bill
    total_amount = 0
    for item in cart_items:
        total_amount += item['quantity'] * item['product'].price

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
        'num_items': len(cart_items),
    }
    return render(request, 'checkout.html', context)
'''


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = Product.objects.get(id=product_id)
    cart[product_id] = product
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse("cart"))


def view_cart(request):
    cart = request.session.get('cart',{})
    return render(request, 'cart.html', {'cart': cart})











'''
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', [])
    cart.append({
        'product_id': product.id,
        'name': product.name,
        'price': product.price
    })
    request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', [])
    if not cart:
        return render(request, 'cart.html', {'cart': [], 'total': 0})
    total = 0
    for i in range(len(cart)):
        total += cart[i]['price']
    return render(request, 'cart.html', {'cart': cart, 'total': total})

'''

'''def view_cart(request):
    cart = request.session.get('cart', [])
    total = 0
    for i in range(len(cart)):
        total += cart[i]['price']
    return render(request, 'cart.html', {'cart': cart, 'total': total})
'''













'''
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if not request.session.get('cart'):
        request.session['cart'] = {}
    if product_id in request.session['cart']:
        request.session['cart'][product_id]['quantity'] += 1
    else:
        request.session['cart'][product_id] = {
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }
    request.session.modified = True
    return redirect('cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    context = {
        'cart': cart,
        'total': total,
    }
    return render(request, 'cart.html', context)

'''























'''

def add_to_cart(request, product_id):
    product = product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': product.price,
            'quantity': 1,
        }
    request.session['cart'] = cart


def checkout(request):
    cart = request.session.get('cart', {})
    total_amount = sum([item['price'] * item['quantity'] for item in cart.values()])
    context = {
        'cart': cart,
        'total_amount': total_amount,
    }
    return render(request, 'checkout.html', context)


def view_cart(request):
    #cart = request.session.get('cart', [])
    products = product.objects.all()
    return render(request, 'view_cart.html', {'products': products})'''