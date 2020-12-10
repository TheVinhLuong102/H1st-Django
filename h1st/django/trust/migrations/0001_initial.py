# Generated by Django 3.1.4 on 2020-12-10 12:06


import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

import model_utils.fields

import json.decoder
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('H1stModel', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name')
    ]

    operations = [
        migrations.CreateModel(
            name='ImmutableDataSet',

            fields=[
                ('uuid',
                 models.UUIDField(
                    db_index=True,
                    default=uuid.uuid4,
                    editable=False,
                    help_text='UUID',
                    primary_key=True,
                    serialize=False,
                    unique=True,
                    verbose_name='UUID')),

                ('schema_specs',
                 models.JSONField(
                    blank=True,
                    decoder=json.decoder.JSONDecoder,
                    default=None,
                    encoder=django.core.serializers.json.DjangoJSONEncoder,
                    help_text='Immutable Data Set Schema Specifications',
                    null=True,
                    verbose_name='Immutable Data Set Schema Specifications')),

                ('created',
                 model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='created')),
                ('modified',
                 model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='modified')),

                ('polymorphic_ctype',
                 models.ForeignKey(
                    editable=False,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='polymorphic_h1sttrust.immutabledataset_set+',
                    to='contenttypes.contenttype'))
            ],

            options={
                'verbose_name': 'Immutable Data Set',
                'verbose_name_plural': 'Immutable Data Sets',
                'db_table': 'H1stTrust_ImmutableDataSet',
                'ordering': ('-modified',),
                'get_latest_by': 'modified',
                'abstract': False,
                'default_related_name': 'immutable_data_sets'
            }
        ),

        migrations.CreateModel(
            name='ImmutableFileStoredDataSet',

            fields=[
                ('immutabledataset_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='immutable_file_stored_data_sets',
                    serialize=False,
                    to='H1stTrust.immutabledataset')),

                ('path',
                 models.CharField(
                    db_index=True,
                    default=None,
                    help_text='Immutable Data Set Directory/File/URL Path',
                    max_length=255,
                    unique=True,
                    verbose_name='Immutable Data Set Directory/File/URL Path'))
            ],

            options={
                'verbose_name': 'Immutable File-Stored Data Set',
                'verbose_name_plural': 'Immutable File-Stored Data Sets',
                'db_table': 'H1stTrust_ImmutableFileStoredDataSet',
                'abstract': False,
                'default_related_name': 'immutable_file_stored_data_sets',
                'base_manager_name': 'objects'
            },

            bases=('H1stTrust.immutabledataset',)
        ),

        migrations.CreateModel(
            name='ImmutableParquetDataSet',

            fields=[
                ('immutablefilestoreddataset_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='immutable_parquet_data_sets',
                    serialize=False,
                    to='H1stTrust.immutablefilestoreddataset'))
            ],

            options={
                'verbose_name': 'Immutable Parquet Data Set',
                'verbose_name_plural': 'Immutable Parquet Data Sets',
                'db_table': 'H1stTrust_ImmutableParquetDataSet',
                'abstract': False,
                'default_related_name': 'immutable_parquet_data_sets',
                'base_manager_name': 'objects'
            },

            bases=('H1stTrust.immutablefilestoreddataset',)
        ),

        migrations.CreateModel(
            name='Decision',

            fields=[
                ('uuid',
                 models.UUIDField(
                    db_index=True,
                    default=uuid.uuid4,
                    editable=False,
                    help_text='UUID',
                    primary_key=True,
                    serialize=False,
                    unique=True,
                    verbose_name='UUID')),

                ('input_data',
                 models.JSONField(
                    blank=True,
                    decoder=json.decoder.JSONDecoder,
                    default=None,
                    encoder=django.core.serializers.json.DjangoJSONEncoder,
                    help_text='Input Data into Decision',
                    null=True,
                    verbose_name='Input Data into Decision')),

                ('model',
                 models.ForeignKey(
                    default=None,
                    help_text='Model producing Decision',
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='decisions',
                    related_query_name='decision',
                    to='H1stModel.model',
                    verbose_name='Model producing Decision')),

                ('model_code',
                 models.JSONField(
                    decoder=json.decoder.JSONDecoder,
                    default=None,
                    encoder=django.core.serializers.json.DjangoJSONEncoder,
                    help_text='Code of Model(s) producing Decision',
                    verbose_name='Code of Model(s) producing Decision')),

                ('output_data',
                 models.JSONField(
                    blank=True,
                    decoder=json.decoder.JSONDecoder,
                    default=None,
                    encoder=django.core.serializers.json.DjangoJSONEncoder,
                    help_text='Output Data from Decision',
                    null=True,
                    verbose_name='Output Data from Decision')),

                ('created',
                 model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='created')),
                ('modified',
                 model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='modified'))
            ],

            options={
                'verbose_name': 'Decision',
                'verbose_name_plural': 'Decisions',
                'db_table': 'H1stTrust_Decision',
                'ordering': ('-modified',),
                'get_latest_by': 'modified',
                'abstract': False,
                'default_related_name': 'decisions'
            }
        ),

        migrations.CreateModel(
            name='ModelEvalMetricsSet',

            fields=[
                ('uuid',
                 models.UUIDField(
                    db_index=True,
                    default=uuid.uuid4,
                    editable=False,
                    help_text='UUID',
                    primary_key=True,
                    serialize=False,
                    unique=True,
                    verbose_name='UUID')),

                ('model',
                 models.ForeignKey(
                    default=None,
                    help_text='Model evaluated',
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='model_eval_metrics_sets',
                    related_query_name='model_eval_metrics_set',
                    to='H1stModel.model',
                    verbose_name='Model evaluated')),

                ('eval_data',
                 models.JSONField(
                    decoder=json.decoder.JSONDecoder,
                    default=None,
                    encoder=django.core.serializers.json.DjangoJSONEncoder,
                    help_text='Data for Evaluation',
                    verbose_name='Data for Evaluation')),

                ('eval_metrics',
                 models.JSONField(
                    decoder=json.decoder.JSONDecoder,
                    default=None,
                    encoder=django.core.serializers.json.DjangoJSONEncoder,
                    help_text='Evaluation Metrics',
                    verbose_name='Evaluation Metrics')),

                ('created',
                 model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='created')),
                ('modified',
                 model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='modified'))
            ],

            options={
                'verbose_name': 'Model Evaluation Metrics Set',
                'verbose_name_plural': 'Model Evaluation Metrics Sets',
                'db_table': 'H1stTrust_ModelEvalMetricsSet',
                'ordering': ('-model__modified', '-modified'),
                'get_latest_by': 'modified',
                'abstract': False,
                'default_related_name': 'model_eval_metrics_sets'
            }
        )
    ]
