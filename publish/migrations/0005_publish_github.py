# Generated by Django 3.0.4 on 2020-04-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0004_auto_20200401_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='publish',
            name='github',
            field=models.CharField(max_length=256, null=True),
        ),
    ]