# Generated by Django 3.2.7 on 2021-10-23 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0042_rename_desciption_element_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='rs_name',
            new_name='jbl_rh_name',
        ),
    ]
