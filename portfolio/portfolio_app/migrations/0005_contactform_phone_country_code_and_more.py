# Generated by Django 4.2.2 on 2024-03-17 01:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio_app", "0004_contactform"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactform",
            name="phone_country_code",
            field=models.CharField(
                choices=[("+91", "+91 - India")], default="+91", max_length=5
            ),
        ),
        migrations.AddField(
            model_name="contactform",
            name="phone_number",
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="contactform",
            name="email",
            field=models.EmailField(max_length=100),
        ),
    ]