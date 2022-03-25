from django.db import models
from pessoa.models import Pessoa
from pessoa.models import Base

''' 
class Base(models.Model):
    criado = models.DateField('Criacao', auto_now_add=True)
    modificado = models.DateField('Atualizacao', auto_now=True)
    ativo = models.BooleanField('Ativo ?', default=True)

    class Meta:
        abstract = True
'''

class Endereco(Base):
    ENDERECO_CHOICES = (
        ('C', 'Casa'),
        ('T', 'Trabalho'),
        ('O', 'Outro'),
    )
    rua = models.CharField('Endereco', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    cep = models.CharField('Cep', max_length=100)
    pais = models.CharField('País', max_length=100)
    tipo_endereco = models.CharField('Tipo_Endereco', max_length=1, choices=ENDERECO_CHOICES)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'

    def __str__(self):
        return self.rua
