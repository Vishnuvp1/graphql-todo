# Generated by Django 4.0.2 on 2022-03-03 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_current_user_todo_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='account',
            new_name='owner',
        ),
    ]