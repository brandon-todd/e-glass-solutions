# Generated by Django 3.2.2 on 2021-05-12 20:55

import django.core.validators
from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('email', models.EmailField(default='', max_length=50)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default=False, max_length=50)),
                ('state', localflavor.us.models.USStateField(default='', max_length=2)),
                ('policy', models.CharField(blank=True, max_length=50, null=True)),
                ('deductible', models.CharField(blank=True, max_length=50, null=True)),
                ('claim_num', models.IntegerField(blank=True, max_length=25, null=True)),
                ('pid_num', models.IntegerField(blank=True, max_length=25, null=True)),
                ('ref_num', models.IntegerField(blank=True, max_length=25, null=True)),
                ('loss_date', models.DateField(blank=True, null=True)),
                ('ticket_num', models.IntegerField(blank=True, max_length=25, null=True)),
                ('wo_num', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_date', models.DateField(blank=True, null=True)),
                ('vin', models.CharField(default='', max_length=30)),
                ('license', models.CharField(blank=True, max_length=20, null=True)),
                ('invoice_cost', models.IntegerField(max_length=7)),
                ('scedule_date', models.DateField(blank=True, null=True)),
                ('timeframe_start', models.TimeField(blank=True, null=True)),
                ('timeframe_end', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': True,
            },
        ),
    ]