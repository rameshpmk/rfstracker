# Generated by Django 3.0.3 on 2020-08-03 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfstracker', '0005_auto_20200802_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsdb',
            name='attachement',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='salesdb',
            name='rfsreqfile',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]