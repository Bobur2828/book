# Generated by Django 5.0.3 on 2024-03-31 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='place',
            new_name='books',
        ),
    ]