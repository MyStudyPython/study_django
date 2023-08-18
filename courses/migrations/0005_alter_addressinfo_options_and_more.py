# Generated by Django 4.2.3 on 2023-08-18 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_alter_addressinfo_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="addressinfo",
            options={
                "ordering": ["pid"],
                "verbose_name": "省市县地址信息",
                "verbose_name_plural": "省市县地址信息",
            },
        ),
        migrations.AlterUniqueTogether(
            name="addressinfo",
            unique_together={("address", "note")},
        ),
        migrations.AlterModelTable(
            name="addressinfo",
            table="address",
        ),
    ]
