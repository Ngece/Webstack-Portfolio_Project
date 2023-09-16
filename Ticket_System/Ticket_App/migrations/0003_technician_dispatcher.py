# Generated by Django 4.2.5 on 2023-09-16 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket_App', '0002_company_company_address_company_company_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technician_name', models.CharField(max_length=100)),
                ('technician_email', models.EmailField(max_length=100)),
                ('technician_phone', models.CharField(max_length=13)),
                ('technician_address', models.CharField(max_length=100)),
                ('technician_city', models.CharField(max_length=100)),
                ('technician_state', models.CharField(max_length=100)),
                ('technician_zip', models.CharField(max_length=5)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ticket_App.company')),
            ],
        ),
        migrations.CreateModel(
            name='Dispatcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatcher_name', models.CharField(max_length=100)),
                ('dispatcher_email', models.EmailField(max_length=100)),
                ('dispatcher_phone', models.CharField(max_length=13)),
                ('dispatcher_address', models.CharField(max_length=100)),
                ('dispatcher_city', models.CharField(max_length=100)),
                ('dispatcher_state', models.CharField(max_length=100)),
                ('dispatcher_zip', models.CharField(max_length=5)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ticket_App.company')),
            ],
        ),
    ]