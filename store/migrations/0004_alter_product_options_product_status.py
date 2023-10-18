# Generated by Django 4.2.5 on 2023-10-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_alter_product_options_product_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ("-created_at",)},
        ),
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("waitingapproval", "waiting approval"),
                    ("active", "Active"),
                    ("deleted", "Deleted"),
                ],
                default="active",
                max_length=50,
            ),
        ),
    ]