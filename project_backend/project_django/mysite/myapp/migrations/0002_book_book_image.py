# Generated by Django 4.2.5 on 2024-01-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='default.jpg', upload_to='book_images/'),
        ),
    ]
