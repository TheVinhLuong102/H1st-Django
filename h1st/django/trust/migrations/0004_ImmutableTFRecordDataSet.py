# Generated by Django 3.1.4 on 2020-12-15 06:14


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = ('H1stTrust', '0003_ImmutableJSONDataSet'),

    operations = \
        migrations.CreateModel(
            name='ImmutableTFRecordDataSet',

            fields=[
                ('immutablefilestoreddataset_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='immutable_tfrecord_data_sets',
                    serialize=False,
                    to='H1stTrust.immutablefilestoreddataset'))
            ],

            options={
                'verbose_name': 'Immutable TensorFlow Record Data Set',
                'verbose_name_plural': 'Immutable TensorFlow Record Data Sets',
                'db_table': 'H1stTrust_ImmutableTFRecordDataSet',
                'abstract': False,
                'default_related_name': 'immutable_tfrecord_data_sets',
                'base_manager_name': 'objects'
            },

            bases=('H1stTrust.immutablefilestoreddataset',)
        ),