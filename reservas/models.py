from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    capacidad_maxima = models.PositiveIntegerField()
    lugar = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='eventos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Atraccion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    capacidad_maxima = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='atracciones/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    atraccion = models.ForeignKey(Atraccion, on_delete=models.CASCADE, null=True, blank=True)
    cantidad_personas = models.PositiveIntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva de {self.cantidad_personas} personas por {self.usuario.username}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    imagen = models.ImageField(upload_to='products/', null=True, blank=True)

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3)

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=(('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')))

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()