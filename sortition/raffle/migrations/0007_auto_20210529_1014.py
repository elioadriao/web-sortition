# Generated by Django 3.1 on 2021-05-29 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raffle', '0006_auto_20210529_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='raffle',
            name='sorted_quota',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cota Sorteada'),
        ),
        migrations.AlterField(
            model_name='raffle',
            name='quotas',
            field=models.IntegerField(default=100, verbose_name='Número de Cotas'),
        ),
        migrations.AlterField(
            model_name='raffle',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner_set', to=settings.AUTH_USER_MODEL, verbose_name='Vencedor'),
        ),
    ]
