# Generated by Django 4.2.3 on 2024-08-16 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.event')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.speaker')),
            ],
        ),
    ]
