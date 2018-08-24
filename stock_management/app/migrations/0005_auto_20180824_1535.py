# Generated by Django 2.1 on 2018-08-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_machinepart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinemodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='machinepart',
            name='id',
        ),
        migrations.AddField(
            model_name='machinepart',
            name='part_id_no',
            field=models.CharField(default='nothing', max_length=200, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machinemodel',
            name='product_no',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
