# Generated by Django 3.1 on 2020-08-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalorienzaehler', '0005_auto_20200831_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='usedcalories',
            name='user',
            field=models.TextField(default='user1'),
        ),
    ]
