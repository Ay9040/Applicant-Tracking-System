# Generated by Django 3.1.1 on 2022-05-02 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity_score', models.DecimalField(decimal_places=8, max_digits=10)),
                ('application_date_time', models.DateTimeField(auto_now=True)),
                ('application_status', models.CharField(choices=[('AP', 'Applied'), ('RE', 'Under Review'), ('SC', 'Scheduled for Interview'), ('AC', 'Accepted'), ('RJ', 'Rejected'), ('PE', 'Pending')], default='AP', max_length=2)),
                ('resume', models.FileField(default='settings.MEDIA_ROOT/resumes/Resume.pdf', upload_to='resumes/')),
                ('annotated_resume_filename', models.CharField(default=None, max_length=10485760, null=True)),
                ('parsed_resume', models.CharField(default=None, max_length=10485760, null=True)),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.applicantdetails')),
            ],
        ),
    ]
