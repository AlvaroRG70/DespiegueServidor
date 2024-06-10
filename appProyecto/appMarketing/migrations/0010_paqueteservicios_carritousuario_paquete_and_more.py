# Generated by Django 4.2.11 on 2024-05-30 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMarketing', '0009_pedido_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaqueteServicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('servicios', models.ManyToManyField(related_name='paquetes', to='appMarketing.servicio')),
            ],
        ),
        migrations.AddField(
            model_name='carritousuario',
            name='paquete',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appMarketing.paqueteservicios'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='paquete_carrito',
            field=models.ManyToManyField(to='appMarketing.paqueteservicios'),
        ),
    ]
