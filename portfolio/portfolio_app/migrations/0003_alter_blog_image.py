# Generated by Django 4.2.2 on 2024-02-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio_app", "0002_blog_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                default="uploads/default-image.jpg", upload_to="uploads/"
            ),
        ),
    ]