# Generated by Django 5.1.2 on 2024-10-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_createpost_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
