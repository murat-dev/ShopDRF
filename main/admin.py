from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 10
    min_num = 1


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImageInline, ]


admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Like)
admin.site.register(Favorite)