# Generated by Django 2.1.3 on 2018-11-20 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tokens", "0004_auto_20181114_1535"),
    ]

    operations = [
        migrations.RenameField(
            model_name="token",
            old_name="gas_token",
            new_name="gas",
        ),
    ]
