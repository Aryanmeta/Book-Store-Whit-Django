# Generated by Django 4.1.2 on 2022-10-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default=1, upload_to='covers/'),
            preserve_default=False,
        ),
    ]