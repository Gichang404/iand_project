# Generated by Django 5.0 on 2023-12-29 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=90)),
                ("category", models.TextField(blank=True, null=True)),
                ("card_image", models.ImageField(upload_to="books/")),
                (
                    "profile_image",
                    models.ImageField(blank=True, null=True, upload_to="profiles/"),
                ),
                ("prologue", models.TextField(blank=True, null=True)),
                ("year_of_life", models.TextField(blank=True, null=True)),
                ("quiz", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Episodes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "episode_number",
                    models.PositiveIntegerField(default=1, help_text="에피소드 번호"),
                ),
                (
                    "scene_number",
                    models.PositiveIntegerField(default=1, help_text="장면 번호"),
                ),
                (
                    "title",
                    models.CharField(default=None, help_text="에피소드 이름", max_length=30),
                ),
                (
                    "image",
                    models.ImageField(
                        default=None, help_text="에피소드 장면 이미지", upload_to="contents/"
                    ),
                ),
                (
                    "voice",
                    models.FileField(
                        default=None, help_text="기본음성", upload_to="voices/"
                    ),
                ),
                (
                    "voice_text",
                    models.CharField(
                        default=None, help_text="음성 대사 텍스트", max_length=30
                    ),
                ),
                (
                    "quiz_text",
                    models.CharField(
                        default=None, help_text="퀴즈 문제 내용", max_length=100
                    ),
                ),
                (
                    "quiz_answer",
                    models.CharField(default=None, help_text="퀴즈 문제 정답", max_length=30),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="episodes",
                        to="playground.book",
                    ),
                ),
            ],
        ),
    ]
