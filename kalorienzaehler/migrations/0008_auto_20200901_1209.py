# Generated by Django 3.1 on 2020-09-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalorienzaehler', '0007_auto_20200831_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='usedcalories',
            name='user',
        ),
    ]