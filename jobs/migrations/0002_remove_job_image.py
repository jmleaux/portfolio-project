# Generated by Django 2.0.2 on 2020-01-09 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
    ]