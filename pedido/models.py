from django.db import models
from pessoa.models import Pessoa
from pessoa.models import Base


class Pedido(Base):
    STATUS_CHOICES = (
        ('PEF', 'Pedido Efetuado'),
        ('PEN', 'Pedido Entregue'),
        ('PPA', 'Pedido Pago'),
        ('PEV', 'Pedido Enviado'),
        ('PCA', 'Pedido Cancelado'),
    )
    numero = models.IntegerField('Numero_Pedido')
    data = models.DateField('Data_Pedido')
    status = models.CharField('Status', max_length=3, choices=STATUS_CHOICES)
    valor = models.DecimalField('Valor', max_digits=5, decimal_places=2)
    pessoa = pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return str(self.numero)
    
