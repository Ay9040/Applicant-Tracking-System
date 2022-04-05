# Generated by Django 3.1.1 on 2022-04-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_categories', models.CharField(choices=[('EN', 'Engineering'), ('SA', 'Sales'), ('BU', 'Business'), ('ET', 'Entertainment'), ('F', 'Food'), ('O', 'Other')], default='EN', max_length=3)),
            ],
        ),
    ]
