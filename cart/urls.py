from django.urls import path
from .views import add_to_cart, remove_from_cart, get_cart

urlpatterns = [
    path('add_to_cart/', add_to_cart, name="add-to-cart"),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name="remove-from-cart"),
    path('get_cart/', get_cart, name='get-cart'),
]
