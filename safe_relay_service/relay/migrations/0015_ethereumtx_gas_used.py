# Generated by Django 2.2 on 2019-04-22 09:58

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("relay", "0014_internaltx_safetxstatus"),
    ]

    operations = [
        migrations.AddField(
            model_name="ethereumtx",
            name="gas_used",
            field=gnosis.eth.django.models.Uint256Field(default=None, null=True),
        ),
    ]
