# Generated by Django 5.0.3 on 2024-03-31 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_alter_books_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='descrtiption',
            new_name='describtion',
        ),
    ]