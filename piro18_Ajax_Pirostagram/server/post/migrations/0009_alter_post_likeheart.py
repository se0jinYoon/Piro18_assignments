# Generated by Django 4.1.5 on 2023-01-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0008_alter_post_likeheart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likeHeart",
            field=models.TextField(default='<i class="fa-regular fa-heart"></i>'),
        ),
    ]
