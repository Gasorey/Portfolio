# Generated by Django 3.0.4 on 2020-04-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0002_auto_20200403_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/certificate/images/'),
        ),
    ]