# Generated by Django 4.1 on 2022-09-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pizza", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pizza",
            name="size",
            field=models.CharField(
                choices=[("1", "small"), ("2", "medium"), ("3", "large")],
                max_length=2,
                verbose_name="Size",
            ),
        ),
    ]
