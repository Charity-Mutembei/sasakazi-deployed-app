# Generated by Django 4.1.3 on 2023-02-13 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sasakazi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age_number',
            field=models.IntegerField(default='18'),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
