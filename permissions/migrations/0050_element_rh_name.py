# Generated by Django 3.2.7 on 2022-02-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0049_alter_element_text_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='rh_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
