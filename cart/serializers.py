from rest_framework import serializers

from .models import CartItem
from product.serializer import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    item_total = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity', 'item_total')

    def get_item_total(self, obj):
        return obj.quantity * obj.product.price
