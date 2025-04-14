from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),  # About page
    path('index/', views.index, name='index'),  # Index page
    path('cart/', views.cart, name='cart'),  # Cart page
    path('redirect/', views.redirect_to_index, name='redirect_to_index'),  # Redirect URL
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),  # Add item to cart
    path('payment/', views.payment, name='payment'),
    path('payment_success/', views.payment_success, name='payment_success'),

]
