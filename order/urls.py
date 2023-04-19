from django.urls import path
from .views import create_order, get_all_orders, cancel_order, complete_order

urlpatterns = [
    path('create_order/', create_order, name="create-order"),
    path('all_orders/', get_all_orders, name='get_all_orders'),
    path('complete_order/<int:order_id>/', complete_order, name='complete-order'),
    path('cancel_order/<int:order_id>/', cancel_order, name='cancel-order'),
]
