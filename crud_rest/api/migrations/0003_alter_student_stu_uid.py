# Generated by Django 4.2.5 on 2023-09-12 13:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_student_stu_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="stu_uid",
            field=models.CharField(
                blank=True, default=uuid.uuid4, max_length=100, null=True
            ),
        ),
    ]
