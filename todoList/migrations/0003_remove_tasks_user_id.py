# Generated by Django 3.1.7 on 2022-03-06 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0002_tasks_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='user_id',
        ),
    ]