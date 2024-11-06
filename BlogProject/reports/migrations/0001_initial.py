# Generated by Django 5.0.7 on 2024-08-24 16:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("comments", "0001_initial"),
        ("posts", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
            fields=[
                ("id",
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name="ID",
                 ),
                 ),
                ("report_type",
                 models.CharField(
                     choices=[
                         ("post",
                          "Post"),
                         ("comment",
                          "Comment")],
                     max_length=7),
                 ),
                ("reason",
                 models.TextField()),
                ("created_at",
                 models.DateTimeField(
                     auto_now_add=True)),
                ("is_resolved",
                 models.BooleanField(
                     default=False)),
                ("comment",
                 models.ForeignKey(
                     blank=True,
                     null=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name="reports",
                     to="comments.comment",
                 ),
                 ),
                ("post",
                 models.ForeignKey(
                     blank=True,
                     null=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name="reports",
                     to="posts.post",
                 ),
                 ),
                ("reported_by",
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name="reports",
                     to=settings.AUTH_USER_MODEL,
                 ),
                 ),
            ],
        ),
    ]
