# Generated by Django 3.2.25 on 2025-03-09 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_person_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['person_name'], 'verbose_name': 'Persones', 'verbose_name_plural': 'Persones'},
        ),
        migrations.AddField(
            model_name='skills',
            name='is_soft_skill',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='skills',
            unique_together={('skill_name', 'is_soft_skill')},
        ),
        migrations.AlterModelTable(
            name='person',
            table='person',
        ),
        migrations.AlterModelTable(
            name='skills',
            table='skills',
        ),
    ]
