# Generated by Django 4.2.6 on 2023-10-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_percentage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Percentage', models.CharField(max_length=100, null=True)),
                ('skill', models.CharField(max_length=100, null=True)),
                ('p_bar', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
