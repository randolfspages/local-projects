# Generated by Django 5.0.1 on 2024-01-14 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='data',
            new_name='date',
        ),
    ]