# Generated by Django 3.2.25 on 2025-02-25 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='student_bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
