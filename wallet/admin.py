from django.contrib import admin
#Importacion de modelos 
from .models import Usuario, Moneda, Transaccion

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'saldo', 'fecha_registro')
    search_fields = ('nombre', 'correo')
    list_filter = ('fecha_registro',)


@admin.register(Moneda)
class MonedaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'simbolo')
    search_fields = ('nombre', 'simbolo')


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'moneda', 'monto', 'tipo_transaccion', 'fecha')
    search_fields = ('usuario__nombre', 'moneda__nombre', 'tipo_transaccion')
    list_filter = ('tipo_transaccion', 'moneda', 'fecha')