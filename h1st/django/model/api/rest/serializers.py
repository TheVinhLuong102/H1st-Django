from rest_framework.serializers import ModelSerializer

from ...models import Model


class H1stModelSerializer(ModelSerializer):
    class Meta:
        model = Model

        fields = \
            'uuid', \
            'created', \
            'modified'
