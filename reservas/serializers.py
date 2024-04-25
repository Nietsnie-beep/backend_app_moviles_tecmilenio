from rest_framework import serializers
from .models import Evento, Atraccion, Reserva, Transaction, Product, PaymentMethod, UserProfile

# Serializer para el modelo Evento
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

# Serializer para el modelo Atraccion
class AtraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atraccion
        fields = '__all__'

# Serializer para el modelo Reserva
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'product', 'user', 'payment_method', 'amount', 'timestamp', 'status']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'user', 'card_number', 'expiry_date', 'cvv']
        extra_kwargs = {
            'cvv': {'write_only': True}  # Ensure CVV is never sent back to the client
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'phone_number', 'address']