# Generated by Django 3.2.25 on 2025-02-25 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20250225_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.college'),
        ),
    ]
