# Generated by Django 3.1.1 on 2020-09-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20200915_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
