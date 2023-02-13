# Generated by Django 4.1.5 on 2023-02-13 16:01

from django.db import migrations, models
import persons.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0013_teacher_on_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=14, validators=[persons.validators.is_phone_number], verbose_name='Телефон'),
        ),
    ]
