# Generated by Django 4.2.5 on 2023-10-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0007_rename_merchant_id_order_payment_intent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/product_images/"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("waitingapproval", "Waiting approval"),
                    ("active", "Active"),
                    ("deleted", "Deleted"),
                ],
                default="active",
                max_length=50,
            ),
        ),
    ]
