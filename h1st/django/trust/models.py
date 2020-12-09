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
from ..model.models import H1stDjangoModel
from ..util import PGSQL_IDENTIFIER_MAX_LEN
from . import H1stTrustAppConfig


class RecordedModelRun(PolymorphicModel):
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
        db_table = f"{H1stTrustAppConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name = 'recorded_model_runs'

        verbose_name = 'Recorded Model Run'
        verbose_name_plural = 'Recorded Model Runs'

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}'


class RecordedModelFittingRun(RecordedModelRun):
    class Meta:
        db_table = f"{H1stTrustAppConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name = 'recorded_model_fitting_runs'

        verbose_name = 'Recorded Model Fitting Run'
        verbose_name_plural = 'Recorded Model Fitting Runs'

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}'


class RecordedModelInferenceRun(RecordedModelRun):
    class Meta:
        db_table = f"{H1stTrustAppConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name = 'recorded_model_inference_runs'

        verbose_name = 'Recorded Model Inference Run'
        verbose_name_plural = 'Recorded Model Inference Runs'

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}'
