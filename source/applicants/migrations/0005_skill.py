# Generated by Django 4.1.7 on 2023-04-22 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0004_resume_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Навык')),
            ],
        ),
    ]