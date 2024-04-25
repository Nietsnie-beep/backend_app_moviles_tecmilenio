from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Evento)
admin.site.register(models.Atraccion)
admin.site.register(models.Reserva)
admin.site.register(models.Product)
admin.site.register(models.PaymentMethod)
admin.site.register(models.Transaction)
admin.site.register(models.UserProfile)