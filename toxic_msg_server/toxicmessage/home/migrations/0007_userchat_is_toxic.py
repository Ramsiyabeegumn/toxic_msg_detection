# Generated by Django 5.0.4 on 2024-04-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_userchat_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchat',
            name='is_toxic',
            field=models.IntegerField(default=0),
        ),
    ]
