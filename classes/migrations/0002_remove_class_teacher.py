# Generated by Django 4.1.5 on 2023-01-17 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
    ]