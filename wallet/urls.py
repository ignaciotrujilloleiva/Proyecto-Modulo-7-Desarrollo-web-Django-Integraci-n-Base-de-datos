from django.urls import path
from .views import (
    InicioView,
    UsuarioListView,
    UsuarioCreateView,
    UsuarioUpdateView,
    UsuarioDeleteView,
    TransaccionListView,
    TransaccionCreateView,
    TransaccionUpdateView,
    TransaccionDeleteView,
)

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),

    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/nuevo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario_delete'),

    path('transacciones/', TransaccionListView.as_view(), name='transaccion_list'),
    path('transacciones/nueva/', TransaccionCreateView.as_view(), name='transaccion_create'),
    path('transacciones/editar/<int:pk>/', TransaccionUpdateView.as_view(), name='transaccion_update'),
    path('transacciones/eliminar/<int:pk>/', TransaccionDeleteView.as_view(), name='transaccion_delete'),
]