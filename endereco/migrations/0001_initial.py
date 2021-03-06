# Generated by Django 3.2.12 on 2022-03-25 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0004_alter_pessoa_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo ?')),
                ('rua', models.CharField(max_length=100, verbose_name='Endereco')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('cep', models.CharField(max_length=100, verbose_name='Cep')),
                ('pais', models.CharField(max_length=100, verbose_name='País')),
                ('tipo_endereco', models.CharField(choices=[('C', 'Casa'), ('T', 'Trabalho'), ('O', 'Outro')], max_length=1, verbose_name='Tipo_Endereco')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoa.pessoa')),
            ],
            options={
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Enderecos',
            },
        ),
    ]
