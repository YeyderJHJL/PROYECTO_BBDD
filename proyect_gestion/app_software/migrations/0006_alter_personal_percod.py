# Generated by Django 5.0.6 on 2024-07-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_software', '0005_alter_personal_percod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='percod',
            field=models.IntegerField(db_column='DNI', primary_key=True, serialize=False, verbose_name='DNI'),
        ),
    ]
