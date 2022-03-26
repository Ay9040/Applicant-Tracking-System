# Generated by Django 3.2.4 on 2022-03-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_categories', models.CharField(choices=[('EN', 'Engineering'), ('SA', 'Sales'), ('BU', 'Business'), ('ET', 'Entertainment'), ('F', 'Food'), ('O', 'Other')], default='EN', max_length=3)),
            ],
        ),
    ]
