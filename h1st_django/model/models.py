from django.db.models.fields import UUIDField

from polymorphic.models import PolymorphicModel

from uuid import uuid4


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
