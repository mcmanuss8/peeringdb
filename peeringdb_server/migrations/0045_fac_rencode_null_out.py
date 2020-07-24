# Generated by Django 2.2.13 on 2020-07-02 19:36

from django.db import migrations


def null_rencode(apps, schema_editor):
    Facility = apps.get_model("peeringdb_server", "Facility")

    for fac in Facility.handleref.all():
        if fac.rencode:
            fac.rencode = ""
            fac.save()


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0044_ixlan_ixf_fields"),
    ]

    operations = [
        migrations.RunPython(null_rencode),
    ]
