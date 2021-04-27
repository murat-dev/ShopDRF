from rest_framework import serializers
from .models import *

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('slug', 'title', )

    def to_representation(self, instance):
        representation = super(CategoryDetailSerializer, self).to_representation(instance)
        return representation

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'stock', 'category', 'images')

    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        user = request.user.profile_designer
        product = Product.objects.create(author=user, **validated_data)
        for image in images_data.getlist('images'):
            ProductImage.objects.create(product=product, image=image)
        return product

    def update(self, instance, validated_data):
        request = self.context.get('request')
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.images.all().delete()
        images_data = request.FILES
        for image in images_data.getlist('images'):
            ProductImage.objects.create(product=instance, image=image)
        return instance

    def to_representation(self, instance):
        representation = super(ProductSerializer, self).to_representation(instance)
        action = self.context.get('action')
        reviews = ReviewSerializer(instance.reviews.all(), many=True).data
        likes = LikeSerializer(instance.likes.filter(like=True), many=True).data
        representation['author'] = instance.author.email
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True, context=self.context).data
        if action == 'list':
            representation['reviews'] = len(reviews)
            representation['likes'] = len(likes)
        if action == 'retrieve':
            representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
            representation['likes'] = LikeSerializer(instance.likes.filter(like=True), many=True).data
            representation['recommends'] = RecommendSerializer(Product.objects.filter(category__exact=instance.category)[:3],
                                                          many=True).data
        return representation


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'product', 'text', )

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user.profile_customer
        review = Review.objects.create(user=user, **validated_data)
        return review

    def to_representation(self, instance):
        representation = super(ReviewSerializer, self).to_representation(instance)
        representation['user'] = instance.user.email
        return representation

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.email
        return representation


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'category', )



class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=500)



