from django.db.models.base import Model
from django.db.models.fields import UUIDField

from model_utils.models import TimeStampedModel

from uuid import uuid4


class DjangoModelWithUUIDPK(Model):
    uuid = \
        UUIDField(
            verbose_name='UUID',
            help_text='UUID',
            default=uuid4,
            primary_key=True, null=False, unique=True,
            blank=False,
            db_index=True,
            editable=False)

    class Meta:
        abstract = True


class DjangoModelWithUUIDPKAndTimestamps(
        DjangoModelWithUUIDPK,
        TimeStampedModel):
    class Meta:
        abstract = True

        get_latest_by = 'modified'

        ordering = '-modified',
