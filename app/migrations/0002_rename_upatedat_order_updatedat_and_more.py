# Generated by Django 4.1.2 on 2022-10-11 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='upatedAt',
            new_name='updatedAt',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='upatedAt',
            new_name='updatedAt',
        ),
    ]