# Generated by Django 3.2.7 on 2021-09-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('age', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('purok_street', models.TextField(max_length=255)),
                ('brgy', models.TextField(max_length=255)),
                ('municipality', models.TextField(max_length=255)),
                ('province', models.TextField(max_length=255)),
                ('ethnicity', models.TextField(max_length=255)),
                ('skill', models.TextField(max_length=255)),
                ('highest_ed_attainment', models.TextField(max_length=255)),
                ('year_graduated', models.TextField(max_length=255)),
                ('degree_course', models.TextField(max_length=255)),
                ('eligibility', models.TextField(max_length=255)),
                ('school_graduated', models.TextField(max_length=255)),
                ('mobile_num', models.IntegerField()),
                ('email_add', models.EmailField(max_length=254)),
                ('afpsat_score', models.IntegerField()),
                ('date_taken', models.DateField()),
                ('occupation', models.TextField(max_length=255)),
                ('reason_application', models.TextField(max_length=255)),
                ('shoes_size', models.CharField(max_length=5)),
                ('tshirt_size', models.TextField(max_length=10)),
                ('short_pants', models.TextField(max_length=10)),
                ('mothers_name', models.TextField(max_length=255)),
                ('fathers_name', models.TextField(max_length=255)),
                ('present_add', models.TextField(max_length=255)),
                ('psa_bcert', models.FileField(upload_to='birth_certificate')),
                ('tor', models.FileField(upload_to='TOR')),
                ('form137', models.FileField(upload_to='Form137')),
                ('body_pic', models.FileField(upload_to='BodyPic')),
                ('cenomar', models.FileField(upload_to='Cenomar')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
