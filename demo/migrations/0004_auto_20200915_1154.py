# Generated by Django 3.1.1 on 2020-09-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
    ]
