# Generated by Django 3.0.2 on 2020-01-29 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('storebase', '0003_auto_20200129_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='aname',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
