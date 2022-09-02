# Generated by Django 4.1 on 2022-09-02 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("postings", "0002_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="free_board",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="postings.freeboardposting",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="notice",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="postings.noticeboardposting",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="operation_board",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="postings.operatingboardposting",
            ),
        ),
    ]