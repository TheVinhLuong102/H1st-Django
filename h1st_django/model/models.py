from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import UUIDField
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey

from polymorphic.models import PolymorphicModel

from json.decoder import JSONDecoder
from uuid import uuid4

from ..data.models import Dataset


class H1stModel(PolymorphicModel):
    uuid = \
        UUIDField(
            verbose_name='UUID',
            default=uuid4,
            primary_key=True,
            null=False,   # implied
            unique=True,   # implied
            db_index=True,
            editable=False)

    def __str__(self):
        return f'{type(self)} #{self.uuid}'


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

    dataset = \
        ForeignKey(
            verbose_name='Dataset',
            to=Dataset,
            on_delete=PROTECT,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            null=False,
            blank=False,
            db_index=True,   # implied
            help_text='Dataset for evaluation')

    eval_metrics = \
        JSONField(
            verbose_name='Evaluation Metrics',
            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,
            null=True,
            blank=True,
            help_text='Evaluation Metrics')

    def __str__(self):
        return f'Evaluation Metrics of {self.h1st_model} on {self.dataset}: ' \
               f'{self.eval_metrics}'
