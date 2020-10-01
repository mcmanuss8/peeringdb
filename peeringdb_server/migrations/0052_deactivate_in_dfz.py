# Generated by Django 2.2.14 on 2020-08-18 07:09

from django.db import migrations, models


def noop_in_dfz(apps, schema_editor):

    IXLanPrefix = apps.get_model("peeringdb_server", "IXLanPrefix")

    for pfx in IXLanPrefix.handleref.filter(in_dfz=False):
        pfx.in_dfz = True
        pfx.save()


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0051_auto_20200730_1622"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ixlanprefix",
            name="in_dfz",
            field=models.BooleanField(default=True),
        ),
        migrations.RunPython(noop_in_dfz),
    ]
