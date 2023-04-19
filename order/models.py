from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk}"

    def total_amount(self):
        return sum(item.subtotal() for item in self.items.all())

    def cancel_order(self):
        if self.status == "PENDING":
            self.status = "CANCELLED"
            self.save()

    def complete_order(self):
        if self.status == "PENDING":
            self.status = "DELIVERED"
            self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.pk}"

    def subtotal(self):
        return self.quantity * self.price


class OrderStatus(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="statuses")
    status = models.CharField(max_length=20, choices=Order.STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status} on Order #{self.order.pk}"
