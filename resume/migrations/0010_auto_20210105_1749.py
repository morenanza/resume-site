# Generated by Django 3.1.5 on 2021-01-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_resume_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='cv',
            field=models.FileField(null=True, upload_to='static/file'),
        ),
    ]