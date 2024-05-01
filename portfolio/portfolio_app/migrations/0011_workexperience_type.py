# Generated by Django 4.2.2 on 2024-04-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio_app", "0010_education_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="workexperience",
            name="type",
            field=models.CharField(
                choices=[
                    ("POR", "POR"),
                    ("professional", "professional"),
                    ("misc", "misc"),
                ],
                default="misc",
                max_length=20,
            ),
        ),
    ]
