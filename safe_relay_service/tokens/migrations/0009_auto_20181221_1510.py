# Generated by Django 2.1.4 on 2018-12-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tokens", "0008_priceoracleticker_inverse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="logo_uri",
            field=models.CharField(max_length=300),
        ),
    ]
