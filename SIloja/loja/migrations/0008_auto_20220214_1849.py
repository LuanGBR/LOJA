# Generated by Django 3.2.9 on 2022-02-14 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loja', '0007_alter_itemcarrinho_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='itemcarrinho',
            name='produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='loja.produto'),
        ),
    ]