# Generated by Django 3.2.4 on 2022-03-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecruiterDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_website', models.URLField(null=True)),
                ('corporate_address', models.TextField(max_length=1000)),
                ('company_description', models.TextField(max_length=500)),
            ],
        ),
    ]
