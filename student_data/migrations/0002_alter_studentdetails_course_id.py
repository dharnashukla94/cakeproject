# Generated by Django 4.1 on 2023-03-03 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student_data.course'),
        ),
    ]
