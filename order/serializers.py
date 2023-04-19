from rest_framework import serializers

from product.serializer import ProductSerializer
from .models import Order, OrderItem, OrderStatus


class OrderItemSerializer(serializers.ModelSerializer):
    product_info = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_info', 'quantity', 'price']


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['status', 'created_at']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    statuses = OrderStatusSerializer(many=True, read_only=True)
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'status', 'created_at', 'updated_at', 'items', 'statuses', 'total_amount']

    def get_total_amount(self, obj):
        return obj.total_amount()

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        statuses_data = validated_data.pop('statuses')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        for status_data in statuses_data:
            OrderStatus.objects.create(order=order, **status_data)

        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        statuses_data = validated_data.pop('statuses', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if items_data is not None:
            OrderItem.objects.filter(order=instance).delete()

            for item_data in items_data:
                OrderItem.objects.create(order=instance, **item_data)

        if statuses_data is not None:
            OrderStatus.objects.filter(order=instance).delete()

            for status_data in statuses_data:
                OrderStatus.objects.create(order=instance, **status_data)

        instance.save()
        return instance
