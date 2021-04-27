from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


MyUser = get_user_model()


class ProfileDesigner(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile_designer')
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=300, default='no bio...')
    avatar = models.ImageField(upload_to='avatars/', default='default-avatar.jpg')
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'{self.user.email}'

    def save(self, *args, **kwargs):
        to_slug = str(self.user.username)
        self.slug = to_slug
        super().save(*args, **kwargs)


class ProfileCustomer(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile_customer')
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        to_slug = str(self.user.username)
        self.slug = to_slug
        super().save(*args, **kwargs)



