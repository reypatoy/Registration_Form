# Generated by Django 3.2.7 on 2021-09-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_client_info_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_info',
            name='degree_course',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
