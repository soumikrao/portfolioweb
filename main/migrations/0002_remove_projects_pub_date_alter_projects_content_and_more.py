# Generated by Django 4.0.4 on 2022-07-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='projects',
            name='content',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
    ]
