from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import UUIDField
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey

from json.decoder import JSONDecoder
from uuid import uuid4

from ..data.models import DataSet
from ..model.models import H1stModel
from ..util import PGSQL_IDENTIFIER_MAX_LEN
from .apps import H1stTrustAppConfig


class Decision(Model):
    RELATED_NAME = 'decisions'
    RELATED_QUERY_NAME = 'decision'

    uuid = \
        UUIDField(
            verbose_name='UUID',
            default=uuid4,
            primary_key=True,
            null=False,   # implied
            unique=True,   # implied
            db_index=True,
            editable=False)

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
            help_text='Data Set used in Decision')

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
            help_text='H1st Model used in Decision')

    output_json = \
        JSONField(
            verbose_name='Output (JSON)',
            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,
            null=True,
            blank=True,
            help_text='Output (JSON) of Decision')

    class Meta:
        db_table = f"{H1stTrustAppConfig.label}_{__qualname__.split('.')[0]}"

        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name = 'decisions'

        verbose_name = 'Decision'
        verbose_name_plural = 'Decisions'

    def __str__(self):
        return f'Decision on {self.data_set} by {self.h1st_model}: ' \
               f'{self.output_json}'
