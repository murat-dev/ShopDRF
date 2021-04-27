from django.db.models import Sum
from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    price = serializers.ReadOnlyField(source='get_total_price')
    class Meta:
        model = CartItem
        fields = ('product', 'amount', 'price')


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, write_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'items', )

    def create(self, validated_data):
        request = self.context.get('request')
        items = validated_data.pop('items')
        user = request.user.profile_customer
        cart = Cart.objects.create(user=user)
        for item in items:
            CartItem.objects.create(cart=cart,
                                    product=item['product'],
                                    amount=item['amount'])
        return cart


    def to_representation(self, instance):
        representation = super(CartSerializer, self).to_representation(instance)
        representation['user'] = instance.user.email
        representation['products'] = CartItemSerializer(instance.cartitem.all(), many=True).data
        return representation


