# Generated by Django 3.1.5 on 2021-01-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20210105_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='cv',
            field=models.FileField(null=True, upload_to='file'),
        ),
    ]
