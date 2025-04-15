import logging
import stripe
import json
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item

# Logger setup
logger = logging.getLogger(__name__)

# Stripe config
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def about(request):
    return render(request, 'about.html')

def index(request):
    coffee_items = Item.objects.filter(category='coffee')
    pizza_items = Item.objects.filter(category='pizza')
    burger_items = Item.objects.filter(category='burger')
    dessert_items = Item.objects.filter(category='dessert')  # Adding desserts
    sandwich_items = Item.objects.filter(category='sandwich')  # Adding sandwiches
    drink_items = Item.objects.filter(category='drink')  # Adding drinks
    pasta_items = Item.objects.filter(category='pasta')  # Adding pasta items
    logger.debug(f"Drink items: {drink_items}")

    items_data = list(coffee_items) + list(pizza_items) + list(burger_items) + \
                 list(dessert_items) + list(sandwich_items) + list(drink_items) + \
                 list(pasta_items)  # Include pasta in the combined list

    items_json = json.dumps([{
        'id': item.id,
        'name': item.name,
        'price': float(item.price) if item.price else 0.0,
        'description': item.description,
        'image': item.image.url if item.image and hasattr(item.image, 'url') else None
    } for item in items_data])

    return render(request, 'index.html', {
        'coffee_items': coffee_items,
        'pizza_items': pizza_items,
        'burger_items': burger_items,
        'dessert_items': dessert_items,  # Add dessert items to context
        'sandwich_items': sandwich_items,  # Add sandwich items to context
        'drink_items': drink_items,  # Add drink items to context
        'pasta_items': pasta_items,  # Add pasta items to context
        'items_json': items_json,
    })

def cart(request):
    cart = request.session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    return render(request, 'cart.html', {'cart_items': cart, 'total': total})

def add_to_cart(request, item_id):
    item = Item.objects.get(id=item_id)
    cart = request.session.get('cart', [])

    for cart_item in cart:
        if cart_item['id'] == item.id:
            cart_item['quantity'] += 1
            break
    else:
        cart.append({
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'quantity': 1,
        })

    request.session['cart'] = cart
    return redirect('cart')

def payment(request):
    # Try to get cart from POST if provided
    if request.method == 'POST' and request.POST.get('cart_data'):
        try:
            cart = json.loads(request.POST['cart_data'])
        except json.JSONDecodeError:
            cart = []
    else:
        cart = request.session.get('cart', [])

    print(f"Cart items: {cart}")
    total = sum(item['price'] * item['quantity'] for item in cart)

    if total == 0:
        print("⚠️ Total is zero! Cart might be empty or items don't have valid prices.")

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Total',
                    },
                    'unit_amount': int(total * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/payment_success/'),
            cancel_url=request.build_absolute_uri('/payment_error/'),
        )

        return render(request, 'payment.html', {
            'total': total,
            'checkout_session_id': session.id,
            'stripe_public_key': settings.STRIPE_TEST_PUBLIC_KEY,
        })

    except Exception as e:
        print("⚠️ Error in payment view:", e)
        return render(request, 'payment_error.html')

@csrf_exempt
def payment_success(request):
    request.session['cart'] = []
    return render(request, 'payment_success.html')

def payment_error(request):
    return render(request, 'payment_error.html')

def redirect_to_index(request):
    return redirect('index')