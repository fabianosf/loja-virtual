# Generated by Django 3.2.12 on 2022-03-24 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoa', '0002_alter_pessoa_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
