# Generated by Django 3.1.1 on 2020-09-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=36, null=True, unique=True),
        ),
    ]
