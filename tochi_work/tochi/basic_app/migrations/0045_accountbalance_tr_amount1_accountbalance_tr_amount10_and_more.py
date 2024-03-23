# Generated by Django 5.0 on 2023-12-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0044_alter_accountbalance_tr_paymentmode1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount1',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount10',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount11',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount12',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount2',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount3',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount4',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount5',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount6',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount7',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount8',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_amount9',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='accountbalance',
            name='tr_paymentmode1',
            field=models.CharField(blank=True, default=1, max_length=20),
        ),
    ]
