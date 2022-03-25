from django.db import models
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Base(models.Model):
    criado = models.DateField('Criacao', auto_now_add=True)
    modificado = models.DateField('Atualizacao', auto_now=True)
    ativo = models.BooleanField('Ativo ?', default=True)

    class Meta:
        abstract = True


class Pessoa(Base):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField('Nome', max_length=150)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    email = models.EmailField('E-mail', max_length=75)
    cpf = CPFField('CPF')
    celular = PhoneNumberField(unique=True, null=False, blank=False)
    data_nascimento = models.DateField('Data de Nascimento')
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome
