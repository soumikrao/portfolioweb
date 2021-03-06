# Generated by Django 4.0.4 on 2022-07-04 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_projects_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='achievements',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=500)),
                ('content', models.TextField(default='', max_length=5000)),
                ('pub_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
