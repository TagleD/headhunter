# Generated by Django 4.1.7 on 2023-04-21 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0004_resume_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=512, verbose_name='Название компании')),
                ('obligations', models.TextField(max_length=4096, verbose_name='Описание работы')),
                ('position', models.CharField(max_length=128, verbose_name='Занимаемая должность')),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')),
                ('ended_at', models.DateTimeField(null=True, verbose_name='Дата окончания')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='applicants.resume', verbose_name='Резюме')),
            ],
            options={
                'verbose_name': 'Опыт',
                'verbose_name_plural': 'Опыт',
            },
        ),
    ]
