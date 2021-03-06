# Generated by Django 3.1.5 on 2021-01-30 01:40

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import json.decoder


class Migration(migrations.Migration):

    dependencies = [
        ('H1stData', '0002_CSVDataSet'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumPyArray',
            fields=[
                ('jsondataset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='numpy_arrays', serialize=False, to='H1stData.jsondataset')),
                ('dtype', models.JSONField(decoder=json.decoder.JSONDecoder, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, help_text='Data Type(s)', verbose_name='Data Type(s)')),
            ],
            options={
                'verbose_name': 'NumPy Array',
                'verbose_name_plural': 'NumPy Arrays',
                'db_table': 'H1stData_NumPyArray',
                'abstract': False,
                'default_related_name': 'numpy_arrays',
                'base_manager_name': 'objects',
            },
            bases=('H1stData.jsondataset',),
        ),
        migrations.CreateModel(
            name='PandasDataFrame',
            fields=[
                ('jsondataset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='pandas_dataframes', serialize=False, to='H1stData.jsondataset')),
            ],
            options={
                'verbose_name': 'Pandas DataFrame',
                'verbose_name_plural': 'Pandas DataFrames',
                'db_table': 'H1stData_PandasDataFrame',
                'abstract': False,
                'default_related_name': 'pandas_dataframes',
                'base_manager_name': 'objects',
            },
            bases=('H1stData.jsondataset',),
        ),
        migrations.CreateModel(
            name='NamedNumPyArray',
            fields=[
                ('numpyarray_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='named_numpy_arrays', serialize=False, to='H1stData.numpyarray')),
                ('name', models.CharField(db_index=True, default=None, help_text='Data Set Unique Name', max_length=255, unique=True, verbose_name='Data Set Unique Name')),
            ],
            options={
                'verbose_name': 'Named NumPy Array',
                'verbose_name_plural': 'Named NumPy Arrays',
                'db_table': 'H1stData_NamedNumPyArray',
                'ordering': ('name',),
                'abstract': False,
                'default_related_name': 'named_numpy_arrays',
                'base_manager_name': 'objects',
            },
            bases=('H1stData.numpyarray', models.Model),
        ),
        migrations.CreateModel(
            name='NamedPandasDataFrame',
            fields=[
                ('pandasdataframe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='named_pandas_dataframes', serialize=False, to='H1stData.pandasdataframe')),
                ('name', models.CharField(db_index=True, default=None, help_text='Data Set Unique Name', max_length=255, unique=True, verbose_name='Data Set Unique Name')),
            ],
            options={
                'verbose_name': 'Named Pandas DataFrame',
                'verbose_name_plural': 'Named Pandas DataFrames',
                'db_table': 'H1stData_NamedPandasDataFrame',
                'ordering': ('name',),
                'abstract': False,
                'default_related_name': 'named_pandas_dataframes',
                'base_manager_name': 'objects',
            },
            bases=('H1stData.pandasdataframe', models.Model),
        ),
    ]
