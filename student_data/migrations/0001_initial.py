# Generated by Django 4.1 on 2023-03-03 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('sid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_data.course')),
            ],
        ),
    ]
