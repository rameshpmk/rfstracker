# Generated by Django 3.0.3 on 2020-08-01 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfstracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsdb',
            name='rfsnumber',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rfstracker.Salesdb'),
        ),
        migrations.AlterField(
            model_name='salesdb',
            name='rfsnumber',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]