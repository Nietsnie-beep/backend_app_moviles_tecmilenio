from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    EventoListCreateView, EventoRetrieveUpdateDestroyView,
    AtraccionListCreateView, AtraccionRetrieveUpdateDestroyView,
    ReservaListCreateView, ReservaRetrieveUpdateDestroyView, TransactionViewSet,ProductViewSet, PaymentMethodViewSet, UserProfileViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'products', ProductViewSet)
router.register(r'payment_methods', PaymentMethodViewSet)
router.register(r'user_profiles', UserProfileViewSet)

urlpatterns = [
    path('eventos/', EventoListCreateView.as_view(), name='evento-list-create'),
    path('eventos/<int:pk>/', EventoRetrieveUpdateDestroyView.as_view(), name='evento-detail'),
    path('atracciones/', AtraccionListCreateView.as_view(), name='atraccion-list-create'),
    path('atracciones/<int:pk>/', AtraccionRetrieveUpdateDestroyView.as_view(), name='atracciones-detail'),
    path('reservas/', ReservaListCreateView.as_view(), name='reserva-list-create'),
    path('reservas/<int:pk>/', ReservaRetrieveUpdateDestroyView.as_view(), name='reserva-detail'),
    path('api/', include(router.urls)), 
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)