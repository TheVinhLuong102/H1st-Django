from rest_framework.fields import Field
from rest_framework.serializers import ModelSerializer

from ...models import Model


class ModelDescriptionField(Field):
    def to_representation(self, value):
        return str(value)


class H1stModelSerializer(ModelSerializer):
    description = \
        ModelDescriptionField(
            read_only=True,
            write_only=False,
            required=False)

    class Meta:
        model = Model

        fields = \
            'description', \
            'uuid', \
            'created', \
            'modified'
