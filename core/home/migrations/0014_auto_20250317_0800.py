# Generated by Django 3.2.25 on 2025-03-17 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_employee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': (('can_do_something', 'Can do something'),)},
        ),
        migrations.AddField(
            model_name='skills',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
