# Generated by Django 4.0.4 on 2022-05-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.TextField(),
        ),
    ]
