# Generated by Django 5.0 on 2023-12-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0025_accountbalance_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount1',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount10',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount11',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount12',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount2',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount3',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount4',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount5',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount6',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount7',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount8',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_amount9',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date10',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date11',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date12',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date3',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date4',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date5',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date6',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date7',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date8',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_date9',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan1',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan10',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan11',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan12',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan2',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan3',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan4',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan5',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan6',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan7',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan8',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_plan9',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type1',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type10',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type11',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type12',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type2',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type3',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type4',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type5',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type6',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type7',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type8',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='pr_type9',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
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
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date10',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date11',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date12',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date3',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date4',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date5',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date6',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date7',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date8',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_date9',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode1',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode10',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode11',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode12',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode2',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode3',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode4',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode5',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode6',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode7',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode8',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_paymentmode9',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status1',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status10',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status11',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status12',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status2',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status3',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status4',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status5',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status6',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status7',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status8',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='tr_status9',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]