# Generated by Django 3.0.2 on 2020-01-30 04:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storebase', '0005_auto_20200129_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='b_author',
            field=models.ForeignKey(default=datetime.datetime(2020, 1, 30, 4, 43, 33, 118999, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='storebase.Author'),
            preserve_default=False,
        ),
    ]
