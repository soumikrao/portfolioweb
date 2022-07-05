# Generated by Django 4.0.4 on 2022-07-04 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_projects_pub_date_alter_projects_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
