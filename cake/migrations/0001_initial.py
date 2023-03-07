# Generated by Django 4.1 on 2023-02-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]