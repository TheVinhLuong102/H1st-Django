from django.db.models.fields import UUIDField

from polymorphic.models import PolymorphicModel

from uuid import uuid4

from ..util import PGSQL_IDENTIFIER_MAX_LEN
from .apps import H1stDataAppConfig


class Dataset(PolymorphicModel):
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

        default_related_name = 'datasets'

        verbose_name = 'Dataset'
        verbose_name_plural = 'Datasets'

    def __str__(self):
        return f'Dataset #{self.uuid}'   # {type(self).__name__}
