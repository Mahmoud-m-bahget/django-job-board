# Generated by Django 3.0.3 on 2020-08-04 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20200804_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
