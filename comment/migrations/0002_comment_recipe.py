# Generated by Django 4.1.3 on 2022-11-23 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0003_recipe_image"),
        ("comment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="recipe",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="recipe.recipe",
            ),
        ),
    ]
