# Generated by Django 4.2.7 on 2024-12-12 23:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("plan_site", "0006_task_plan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="file",
            field=models.FileField(null=True, upload_to="reports/"),
        ),
    ]
