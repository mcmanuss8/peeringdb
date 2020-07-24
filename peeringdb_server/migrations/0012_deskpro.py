# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-25 16:00


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0011_commandline_tool"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeskProTicket",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("published", models.DateTimeField(null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="userorgaffiliationrequest",
            options={
                "verbose_name": "User to Organization Affiliation Request",
                "verbose_name_plural": "User to Organization Affiliation Requests",
            },
        ),
    ]
