# Generated by Django 3.1 on 2020-08-31 17:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kalorienzaehler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedcalories',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]