# Generated by Django 5.1.2 on 2024-10-17 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dash', '0005_alter_customuser_is_active_alter_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
