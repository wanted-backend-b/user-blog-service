# Generated by Django 4.1 on 2022-09-02 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="free_board",
        ),
        migrations.RemoveField(
            model_name="user",
            name="notice",
        ),
        migrations.RemoveField(
            model_name="user",
            name="operation_board",
        ),
    ]
