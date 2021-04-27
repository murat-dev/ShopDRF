from django.db import models
from myprofile.models import ProfileCustomer
from main.models import Product


class Cart(models.Model):
    user = models.ForeignKey(ProfileCustomer, on_delete=models.CASCADE, related_name='cart')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitem')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitem')
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.title

    def get_total_price(self):
        return self.product.price * self.amount





