# Generated by Django 5.0 on 2023-12-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0028_accountbalance_pr_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbalance',
            name='tr_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
