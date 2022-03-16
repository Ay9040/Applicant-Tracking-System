# Generated by Django 3.2.4 on 2022-03-16 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_job_posts', '0001_initial'),
        ('core_recruiter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposts',
            name='recruiter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_recruiter.recruiterdetails'),
        ),
    ]
