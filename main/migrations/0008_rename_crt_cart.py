# Generated by Django 4.2 on 2023-05-08 09:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_crt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crt',
            new_name='Cart',
        ),
    ]