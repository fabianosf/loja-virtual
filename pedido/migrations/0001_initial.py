# Generated by Django 3.2.12 on 2022-03-25 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0004_alter_pessoa_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo ?')),
                ('numero', models.IntegerField(verbose_name='Numero_Pedido')),
                ('data', models.DateField(verbose_name='Data de Nascimento')),
                ('status', models.CharField(choices=[('PEF', 'Pedido Efetuado'), ('PEN', 'Pedido Entregue'), ('PPA', 'Pedido Pago'), ('PEV', 'Pedido Enviado'), ('PCA', 'Pedido Cancelado')], max_length=3, verbose_name='Status')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoa.pessoa')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]