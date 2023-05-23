# Generated by Django 4.2 on 2023-04-24 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wearssize', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('img', models.ImageField(upload_to='product')),
                ('price', models.CharField(max_length=12)),
                ('description', models.TextField()),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('popular', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]