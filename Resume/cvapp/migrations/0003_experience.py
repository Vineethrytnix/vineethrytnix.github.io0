# Generated by Django 4.2.6 on 2023-10-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0002_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=100, null=True)),
                ('year', models.CharField(max_length=100, null=True)),
                ('desc', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
