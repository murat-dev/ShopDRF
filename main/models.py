from django.contrib.auth import get_user_model
from django.db import models
from myprofile.models import ProfileDesigner, ProfileCustomer

MyUser = get_user_model()

class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


STOCK_CHOICES = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

class Product(models.Model):
    author = models.ForeignKey(ProfileDesigner, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.CharField(max_length=20, choices=STOCK_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}-{self.created}'

    def info_for_bot(self):
        return f'Название: {self.title}\nОписание: {self.description}\nЦена: {self.price} сом\nВ наличии: {self.stock}'

    class Meta:
        ordering = ('-created', )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/')


class Review(models.Model):
    user = models.ForeignKey(ProfileCustomer, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.product}'

    class Meta:
        ordering = ('-created', )


class Like(models.Model):
    user = models.ForeignKey(ProfileCustomer, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)

class Favorite(models.Model):
    user = models.ForeignKey(ProfileCustomer, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField(default=False)


