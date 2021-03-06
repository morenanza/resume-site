# Generated by Django 3.1.5 on 2021-01-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210105_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('when', models.CharField(max_length=30)),
                ('where', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('when', models.CharField(max_length=30)),
                ('where', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='percentage',
        ),
        migrations.AddField(
            model_name='resume',
            name='education',
            field=models.ManyToManyField(to='resume.Education'),
        ),
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.ManyToManyField(to='resume.Experience'),
        ),
    ]
