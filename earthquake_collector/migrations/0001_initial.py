# Generated by Django 2.1.4 on 2018-12-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeismicRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('device_id', models.CharField(max_length=255)),
                ('amplitude', models.CharField(max_length=255)),
                ('added_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
