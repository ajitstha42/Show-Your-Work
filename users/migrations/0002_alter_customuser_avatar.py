# Generated by Django 5.0 on 2024-02-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='idefault.jpg', upload_to='images/'),
        ),
    ]