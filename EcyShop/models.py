from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    origin = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_percentage = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Order(models.Model):
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    amount_of_items = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order ID: {self.pk}"


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    total_amount_spent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    total_orders_completed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Details"
