# Generated by Django 3.2.8 on 2021-11-18 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_categories_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['id'], 'verbose_name': 'Categories', 'verbose_name_plural': 'Categories'},
        ),
    ]