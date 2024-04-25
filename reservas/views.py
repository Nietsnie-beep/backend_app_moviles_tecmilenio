from rest_framework import generics, viewsets
from .models import Evento, Atraccion, Reserva, Transaction, Product, PaymentMethod, UserProfile
from .serializers import EventoSerializer, AtraccionSerializer, ReservaSerializer, TransactionSerializer, ProductSerializer, PaymentMethodSerializer, UserProfileSerializer

# Vistas CRUD para el modelo Evento
class EventoListCreateView(generics.CreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

# Vistas CRUD para el modelo Atraccion
class AtraccionListCreateView(generics.ListCreateAPIView):
    queryset = Atraccion.objects.all()
    serializer_class = AtraccionSerializer

class AtraccionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atraccion.objects.all()
    serializer_class = AtraccionSerializer

# Vistas CRUD para el modelo Reserva
class ReservaListCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer