import random
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Size, Type
from .forms import LoginForm, RegisterForm, OrderForm


def main(request):
    types = Type.objects.all()
    male_trends = Item.objects.filter(gender__in=['male', 'unisex']).order_by('?')[:8]
    female_trends = Item.objects.filter(gender__in=['female', 'unisex']).order_by('?')[:8]
    return render(request, 'main.html', {
        'types': types,
        'male_trends': male_trends,
        'female_trends': female_trends,
    })


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    all_items = list(Item.objects.exclude(id=item_id))
    random_items = random.sample(all_items, min(len(all_items), 8))
    return render(request, 'item_detail.html', {'item': item, 'random_items': random_items})


def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')


def catalog_view(request):
    male_types = Type.objects.filter(items__gender='male').distinct().prefetch_related('items__images')
    female_types = Type.objects.filter(items__gender='female').distinct().prefetch_related('items__images')

    return render(request, 'catalog.html', {
        'male_types': male_types,
        'female_types': female_types,
    })


def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total_price = 0

    for item_id, entry in cart.items():
        item = get_object_or_404(Item, id=item_id)

        # Якщо entry — просто число, то це старий формат
        if isinstance(entry, int):
            entry = {'qty': entry, 'size_id': None}
            cart[item_id] = entry  # оновлюємо на новий формат

        qty = entry.get('qty', 1)
        size_id = entry.get('size_id')
        size = Size.objects.filter(id=size_id).first()
        total = item.price * qty
        total_price += total

        items.append({
            'item': item,
            'qty': qty,
            'total': total,
            'size': size,
        })

    if request.method == 'POST':
        for entry in items:
            size_id = request.POST.get(f'sizes_{entry["item"].id}')
            if size_id:
                cart[str(entry["item"].id)]['size_id'] = int(size_id)
        request.session['cart'] = cart

        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            request.session['cart'] = {}
            return render(request, 'order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'cart.html', {
        'items': items,
        'total_price': total_price,
        'form': form
    })


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart.pop(str(item_id), None)
    request.session['cart'] = cart
    return redirect('cart')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('showcase')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'register/login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('showcase')
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = RegisterForm()

    return render(request, 'register/registration.html', {'form': form})

