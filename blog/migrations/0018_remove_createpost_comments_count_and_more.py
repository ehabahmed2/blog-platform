# Generated by Django 5.1.2 on 2024-10-22 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_createpost_comments_count_createpost_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createpost',
            name='comments_count',
        ),
        migrations.RemoveField(
            model_name='createpost',
            name='likes',
        ),
    ]
