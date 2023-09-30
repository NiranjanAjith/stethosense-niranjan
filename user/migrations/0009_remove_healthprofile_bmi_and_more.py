# Generated by Django 4.2.5 on 2023-09-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_healthprofile_bmi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthprofile',
            name='bmi',
        ),
        migrations.RemoveField(
            model_name='healthprofile',
            name='calories',
        ),
        migrations.AlterField(
            model_name='healthprofile',
            name='emergency_contact',
            field=models.CharField(blank=True, help_text='Emergency contact number', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='healthprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='health_profiles/'),
        ),
    ]