# Generated by Django 3.0.3 on 2020-07-31 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salesdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfsnumber', models.CharField(max_length=254)),
                ('oppnumber', models.CharField(max_length=254)),
                ('description', models.CharField(max_length=254)),
                ('datecreated', models.DateField(auto_now=True)),
                ('rfsreqfile', models.FileField(upload_to='')),
                ('queue', models.CharField(choices=[('sales', 'Sales Queue'), ('solutions', 'Solutions Queue'), ('projectmgmt', 'ProjectMgmt Queue'), ('servicemgmt', 'ServiceMgmt Queue'), ('pricing', 'Pricing Queue'), ('completed', 'Completed Queue')], default='sales', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Detailsdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datecreated', models.DateField(auto_now=True)),
                ('comments', models.CharField(max_length=2000)),
                ('attachement', models.FileField(upload_to='')),
                ('queue', models.CharField(choices=[('sales', 'Sales Queue'), ('solutions', 'Solutions Queue'), ('projectmgmt', 'ProjectMgmt Queue'), ('servicemgmt', 'ServiceMgmt Queue'), ('pricing', 'Pricing Queue'), ('completed', 'Completed Queue')], default='sales', max_length=50)),
                ('rfsnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfstracker.Salesdb')),
            ],
        ),
    ]