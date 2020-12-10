from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey

from polymorphic.models import PolymorphicModel

from json.decoder import JSONDecoder

from ..model.models import H1stModel
from ..util import PGSQL_IDENTIFIER_MAX_LEN
from ..util.models import DjangoModelWithUUIDPKAndTimestamps
from . import H1stTrustModuleConfig


class ImmutableDataSet(PolymorphicModel, DjangoModelWithUUIDPKAndTimestamps):
    schema_specs = \
        JSONField(
            verbose_name='Immutable Data Set Schema Specifications',
            help_text='Immutable Data Set Schema Specifications',
            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,
            null=True,
            blank=True,
            default=None,
            editable=True)

    class Meta(DjangoModelWithUUIDPKAndTimestamps.Meta):
        verbose_name = 'Immutable Data Set'
        verbose_name_plural = 'Immutable Data Sets'

        db_table = \
            f"{H1stTrustModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'immutable_data_sets'

    def __str__(self) -> str:
        return f'{type(self).__name__} #{self.uuid}'


class ImmutableFileStoredDataSet(ImmutableDataSet):
    path = \
        CharField(
            verbose_name='Immutable Data Set Directory/File/URL Path',
            help_text='Immutable Data Set Directory/File/URL Path',
            max_length=255,
            null=False,
            blank=False,
            db_index=True,
            default=None,
            editable=True,
            unique=True)

    class Meta(ImmutableDataSet.Meta):
        verbose_name = 'Immutable File-Stored Data Set'
        verbose_name_plural = 'Immutable File-Stored Data Sets'

        db_table = \
            f"{H1stTrustModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'immutable_file_stored_data_sets'

    def __str__(self) -> str:
        return f'{type(self).__name__} #{self.uuid} @ {self.path}'


class ImmutableParquetDataSet(ImmutableFileStoredDataSet):
    class Meta(ImmutableFileStoredDataSet.Meta):
        verbose_name = 'Immutable Parquet Data Set'
        verbose_name_plural = 'Immutable Parquet Data Sets'

        db_table = \
            f"{H1stTrustModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'immutable_parquet_data_sets'


class Decision(DjangoModelWithUUIDPKAndTimestamps):
    RELATED_NAME = 'decisions'
    RELATED_QUERY_NAME = 'decision'

    input_data = \
        JSONField(
            verbose_name='Input Data into Decision',
            help_text='Input Data into Decision',
            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,
            null=True,
            blank=True,
            default=None,
            editable=True)

    model = \
        ForeignKey(
            verbose_name='Model producing Decision',
            help_text='Model producing Decision',
            to=H1stModel,
            on_delete=PROTECT,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            null=False,
            blank=False,
            db_index=True,   # implied
            default=None,
            editable=True)

    model_code = \
        JSONField(
            verbose_name='Code of Model(s) producing Decision',
            help_text='Code of Model(s) producing Decision',
            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,
            null=False,
            blank=False,
            default=None,
            editable=True)

    output_data = \
        JSONField(
            verbose_name='Output Data from Decision',
            help_text='Output Data from Decision',
            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,
            null=True,
            blank=True,
            default=None,
            editable=True)

    class Meta(DjangoModelWithUUIDPKAndTimestamps.Meta):
        verbose_name = 'Decision'
        verbose_name_plural = 'Decisions'

        db_table = \
            f"{H1stTrustModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'decisions'

    def __str__(self) -> str:
        return f'{type(self).__name__} #{self.uuid} ' \
               f'on {self.input_data} by {self.model}: {self.output_data}'


class ModelEvalMetricsSet(DjangoModelWithUUIDPKAndTimestamps):
    RELATED_NAME = 'model_eval_metrics_sets'
    RELATED_QUERY_NAME = 'model_eval_metrics_set'

    model = \
        ForeignKey(
            verbose_name='Model evaluated',
            help_text='Model evaluated',
            to=H1stModel,
            on_delete=PROTECT,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            null=False,
            blank=False,
            db_index=True,   # implied
            default=None,
            editable=True)

    eval_data = \
        JSONField(
            verbose_name='Data for Evaluation',
            help_text='Data for Evaluation',
            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,
            null=False,
            blank=False,
            default=None,
            editable=True)

    eval_metrics = \
        JSONField(
            verbose_name='Evaluation Metrics',
            help_text='Evaluation Metrics',
            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,
            null=False,
            blank=False,
            default=None,
            editable=True)

    class Meta(DjangoModelWithUUIDPKAndTimestamps.Meta):
        verbose_name = 'Model Evaluation Metrics Set'
        verbose_name_plural = 'Model Evaluation Metrics Sets'

        db_table = \
            f"{H1stTrustModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'model_eval_metrics_sets'

        ordering = '-model__modified', '-modified'

    def __str__(self) -> str:
        return f'Evaluation Metric Set #{self.uuid} of {self.h1st_model}: ' \
               f'{self.eval_metrics}'
