# Generated by Django 2.1.5 on 2019-01-15 12:46

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("relay", "0006_remove_safecreation_payment_ether"),
    ]

    operations = [
        migrations.AddField(
            model_name="safecreation",
            name="master_copy",
            field=gnosis.eth.django.models.EthereumAddressField(
                default="0x8942595A2dC5181Df0465AF0D7be08c8f23C93af"
            ),
            preserve_default=False,
        ),
    ]
