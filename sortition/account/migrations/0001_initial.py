# Generated by Django 3.1 on 2021-05-31 14:41

from django.db import migrations, models
import django.db.models.deletion
import sortition.account.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255, verbose_name='Rua')),
                ('number', models.CharField(max_length=8, verbose_name='Número')),
                ('neighborhood', models.CharField(max_length=255, verbose_name='Bairro')),
                ('city', models.CharField(max_length=255, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('whatsapp', models.CharField(max_length=11, unique=True, verbose_name='Whatsapp')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('profile', models.ImageField(blank=True, null=True, upload_to=sortition.account.models.get_upload_to, verbose_name='Imagem de Perfil')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Administrador')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.address', verbose_name='Endereço')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]
