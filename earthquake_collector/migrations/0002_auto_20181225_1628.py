# Generated by Django 2.1.4 on 2018-12-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthquake_collector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeismicNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amplitude', models.IntegerField(default=5)),
            ],
        ),
        migrations.AlterField(
            model_name='seismicrecord',
            name='amplitude',
            field=models.IntegerField(default=5),
        ),
    ]
