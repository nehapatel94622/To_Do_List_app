# Generated by Django 4.0.6 on 2022-09-05 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_task_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='User',
            new_name='user',
        ),
    ]
