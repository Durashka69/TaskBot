# Generated by Django 4.1.5 on 2023-01-12 14:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_like_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="like",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
