# Generated by Django 4.2 on 2025-06-04 12:31

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_loan_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='due_date',
            field=models.DateField(default=library.models.default_date),
        ),
    ]
