# Generated by Django 4.0.3 on 2022-04-01 13:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_applicant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_degree', models.CharField(choices=[('B', 'Bachelors'), ('M', 'MASTERS'), ('PHD', 'PhD')], default='B', max_length=3)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('graduation_year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(1900)])),
                ('university', models.CharField(max_length=250)),
                ('field_of_study', models.CharField(max_length=250)),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_applicant.applicantdetails')),
            ],
        ),
    ]
