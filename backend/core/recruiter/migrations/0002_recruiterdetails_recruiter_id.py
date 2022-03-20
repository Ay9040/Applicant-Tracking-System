# Generated by Django 3.2.4 on 2022-03-20 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_recruiter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterdetails',
            name='recruiter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
