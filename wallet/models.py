from django.db import models

# Create your models here.

from django.db import models

# Creación de los 3 principales modelos (usuario, moneda y transacciones)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Moneda(models.Model):
    nombre = models.CharField(max_length=50)
    simbolo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} ({self.simbolo})"


class Transaccion(models.Model):
    TIPO_TRANSACCION = [
        ('deposito', 'Depósito'),
        ('retiro', 'Retiro'),
        ('transferencia', 'Transferencia'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='transacciones')
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name='transacciones')
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_transaccion = models.CharField(max_length=20, choices=TIPO_TRANSACCION)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.tipo_transaccion} - {self.monto}"