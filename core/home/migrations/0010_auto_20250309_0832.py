# Generated by Django 3.2.25 on 2025-03-09 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_person_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['person_name']},
        ),
        migrations.AlterModelTable(
            name='person',
            table='person',
        ),
    ]
