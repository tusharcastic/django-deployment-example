# Generated by Django 2.1.4 on 2019-01-04 03:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videotitle', models.CharField(max_length=30)),
                ('videodesc', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
