# Generated by Django 4.2.11 on 2024-05-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(null=True),
        ),
    ]
