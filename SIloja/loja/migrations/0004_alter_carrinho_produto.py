# Generated by Django 3.2.9 on 2022-02-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_carrinho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='produto',
            field=models.ManyToManyField(blank=True, to='loja.Produto'),
        ),
    ]
