# Generated by Django 3.2.7 on 2021-10-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0040_auto_20210928_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='jbl_rh_name',
            new_name='rs_name',
        ),
        migrations.AddField(
            model_name='element',
            name='desciption',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='element',
            name='imag_calc_name',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]
