# Generated by Django 5.1b1 on 2024-07-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_networks_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogicon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.URLField()),
                ('icon', models.TextField(max_length=15)),
            ],
        ),
    ]