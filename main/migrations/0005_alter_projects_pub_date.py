# Generated by Django 4.0.4 on 2022-07-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_projects_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
