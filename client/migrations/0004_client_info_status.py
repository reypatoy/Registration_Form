# Generated by Django 3.2.7 on 2021-09-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20210918_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_info',
            name='status',
            field=models.CharField(max_length=255, null=True),
        ),
    ]