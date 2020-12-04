from django.db.models.deletion import PROTECT
from django.db.models.fields import UUIDField
from django.db.models.fields.related import ForeignKey

from polymorphic.models import PolymorphicModel

from uuid import uuid4

from ..util import PGSQL_IDENTIFIER_MAX_LEN
from . import H1stDataAppConfig


class DataSchema(PolymorphicModel):
    uuid = \
        UUIDField(
            verbose_name='UUID',
            default=uuid4,
            primary_key=True,
            null=False,   # implied
            unique=True,   # implied
            db_index=True,
            editable=False)

    class Meta:
        db_table = f"{H1stDataAppConfig.label}_{__qualname__.split('.')[0]}"

        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name = 'data_schemas'

        verbose_name = 'Data Schema'
        verbose_name_plural = 'Data Schemas'

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}'


class DataSet(PolymorphicModel):
    RELATED_NAME = 'data_sets'
    RELATED_QUERY_NAME = 'data_set'

    uuid = \
        UUIDField(
            verbose_name='UUID',
            default=uuid4,
            primary_key=True,
            null=False,   # implied
            unique=True,   # implied
            db_index=True,
            editable=False)

    schema = \
        ForeignKey(
            verbose_name='Schema',
            to=DataSchema,
            on_delete=PROTECT,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            null=True,
            blank=True,
            db_index=True,   # implied
            help_text='Schema')

    class Meta:
        db_table = f"{H1stDataAppConfig.label}_{__qualname__.split('.')[0]}"

        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name = 'data_sets'

        verbose_name = 'Data Set'
        verbose_name_plural = 'Data Sets'

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}'
