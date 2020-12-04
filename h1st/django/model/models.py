from h1st.core.model import Model as H1stCoreModel

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import UUIDField
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey

from polymorphic.models import PolymorphicModel

from json.decoder import JSONDecoder
from uuid import uuid4

from ..data.models import DataSet
from ..util import PGSQL_IDENTIFIER_MAX_LEN
from .apps import H1stModelAppConfig


class H1stModel(PolymorphicModel, H1stCoreModel):
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
        db_table = f"{H1stModelAppConfig.label}_{__qualname__.split('.')[0]}"

        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name = 'h1st_models'

        verbose_name = 'H1st Model'
        verbose_name_plural = 'H1st Models'

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}'


# alias
H1stDjangoModel = H1stModel


class H1stModelEvalMetricsSet(Model):
    RELATED_NAME = 'h1st_model_eval_metrics_sets'
    RELATED_QUERY_NAME = 'h1st_model_eval_metrics_set'

    uuid = \
        UUIDField(
            verbose_name='UUID',
            default=uuid4,
            primary_key=True,
            null=False,   # implied
            unique=True,   # implied
            db_index=True,
            editable=False)

    h1st_model = \
        ForeignKey(
            verbose_name='H1st Model',
            to=H1stModel,
            on_delete=PROTECT,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            null=False,
            blank=False,
            db_index=True,   # implied
            help_text='H1st Model evaluated')

    data_set = \
        ForeignKey(
            verbose_name='Data Set',
            to=DataSet,
            on_delete=PROTECT,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            null=False,
            blank=False,
            db_index=True,   # implied
            help_text='Data Set for evaluation')

    eval_metrics = \
        JSONField(
            verbose_name='Evaluation Metrics',
            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,
            null=False,
            blank=False,
            help_text='Evaluation Metrics')

    class Meta:
        db_table = f"{H1stModelAppConfig.label}_{__qualname__.split('.')[0]}"

        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name = 'h1st_model_eval_metrics_sets'

        verbose_name = 'H1st Model Evaluation Metrics Set'
        verbose_name_plural = 'H1st Model Evaluation Metrics Sets'

    def __str__(self):
        return f'Evaluation Metrics of {self.h1st_model} on {self.data_set}: '\
               f'{self.eval_metrics}'
