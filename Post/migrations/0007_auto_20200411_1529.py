# Generated by Django 2.0.6 on 2020-04-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_auto_20200410_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post_img/default.png', upload_to='post_img/'),
        ),
    ]
