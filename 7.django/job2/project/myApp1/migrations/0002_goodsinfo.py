# Generated by Django 3.1.5 on 2021-01-11 03:39

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
    ]
