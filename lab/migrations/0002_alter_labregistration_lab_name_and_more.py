# Generated by Django 4.2.5 on 2023-10-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lab", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="labregistration",
            name="lab_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="labregistration",
            name="lab_owner",
            field=models.CharField(max_length=100),
        ),
    ]
