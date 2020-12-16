from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey, OneToOneField

from polymorphic.models import PolymorphicModel

from json.decoder import JSONDecoder

from ..util import PGSQL_IDENTIFIER_MAX_LEN
from ..util.models import _ModelWithUUIDPKAndTimestamps
from .apps import H1stDataModuleConfig


class DataSchema(PolymorphicModel, _ModelWithUUIDPKAndTimestamps):
    name = \
        CharField(
            verbose_name='Data Schema Unique Name',
            help_text='Data Schema Unique Name',

            max_length=255,

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=True,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    specs = \
        JSONField(
            verbose_name='Data Schema Specifications',
            help_text='Data Schema Specifications',

            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=False,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(_ModelWithUUIDPKAndTimestamps.Meta):
        verbose_name = 'Data Schema'
        verbose_name_plural = 'Data Schemas'

        db_table = f"{H1stDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'data_schemas'

        ordering = 'name',

    def __str__(self) -> str:
        return f'"{self.name}" {type(self).__name__}'


class DataSet(PolymorphicModel, _ModelWithUUIDPKAndTimestamps):
    RELATED_NAME = 'data_sets'
    RELATED_QUERY_NAME = 'data_set'

    schema = \
        ForeignKey(
            verbose_name='Data Set Schema',
            help_text='Data Set Schema',

            to=DataSchema,
            on_delete=SET_NULL,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(_ModelWithUUIDPKAndTimestamps.Meta):
        verbose_name = 'Data Set'
        verbose_name_plural = 'Data Sets'

        db_table = f"{H1stDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'data_sets'

    def __str__(self) -> str:
        return f'{type(self).__name__} #{self.uuid}'


class NamedDataSet(DataSet):
    RELATED_NAME = 'named_data_sets'
    RELATED_QUERY_NAME = 'named_data_set'

    name = \
        CharField(
            verbose_name='Data Set Unique Name',
            help_text='Data Set Unique Name',

            max_length=255,

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=True,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(DataSet.Meta):
        verbose_name = 'Named Data Set'
        verbose_name_plural = 'Named Data Sets'

        db_table = f"{H1stDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'named_data_sets'

        ordering = 'name',

    def __str__(self) -> str:
        return f'"{self.name}" {type(self).__name__}'


class JSONDataSet(DataSet):
    json = \
        JSONField(
            verbose_name='JSON Data Content',
            help_text='JSON Data Content',

            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=False,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(DataSet.Meta):
        verbose_name = 'JSON Data Set'
        verbose_name_plural = 'JSON Data Sets'

        db_table = f"{H1stDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'json_data_sets'


class NamedJSONDataSet(NamedDataSet, JSONDataSet):
    class Meta(NamedDataSet.Meta, JSONDataSet.Meta):
        verbose_name = 'Named JSON Data Set'
        verbose_name_plural = 'Named JSON Data Sets'

        db_table = f"{H1stDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'named_json_data_sets'


class FileStoredDataSet(DataSet):
    path = \
        CharField(
            verbose_name='Data Set Directory/File/URL Path',
            help_text='Data Set Directory/File/URL Path',
            max_length=255,
            null=False,
            blank=False,
            db_index=True,
            default=None,
            editable=True,
            unique=False)

    class Meta(DataSet.Meta):
        verbose_name = 'File-Stored Data Set'
        verbose_name_plural = 'File-Stored Data Sets'

        db_table = f"{H1stDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'file_stored_data_sets'

    def __str__(self) -> str:
        return f'"{self.name}" {type(self).__name__} @ {self.path}'


class ParquetDataSet(FileStoredDataSet):
    class Meta(FileStoredDataSet.Meta):
        verbose_name = 'Parquet Data Set'
        verbose_name_plural = 'Parquet Data Sets'

        db_table = f"{H1stDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'parquet_data_sets'


class TFRecordDataSet(FileStoredDataSet):
    class Meta(FileStoredDataSet.Meta):
        verbose_name = 'TensorFlow Record Data Set'
        verbose_name_plural = 'TensorFlow Record Data Sets'

        db_table = f"{H1stDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'tfrecord_data_sets'
