# Generated by Django 3.0.2 on 2020-01-30 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storebase', '0006_book_b_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='b_author',
        ),
    ]
