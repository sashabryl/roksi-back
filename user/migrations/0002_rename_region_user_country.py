# Generated by Django 4.2.9 on 2024-02-15 15:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="region",
            new_name="country",
        ),
    ]
