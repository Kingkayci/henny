# Generated by Django 5.0 on 2023-12-16 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0042_alter_accountbalance_t_amount2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount1',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount10',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount11',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount12',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount2',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount3',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount4',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount5',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount6',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount7',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount8',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='t_amount9',
        ),
    ]