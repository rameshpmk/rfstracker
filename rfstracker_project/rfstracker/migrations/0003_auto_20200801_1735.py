# Generated by Django 3.0.3 on 2020-08-01 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfstracker', '0002_auto_20200801_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsdb',
            name='rfsnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfstracker.Salesdb'),
        ),
    ]
