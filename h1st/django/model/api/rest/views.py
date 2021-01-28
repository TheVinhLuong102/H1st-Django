from rest_framework.authentication import \
    BasicAuthentication, \
    RemoteUserAuthentication, \
    SessionAuthentication, \
    TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import CoreJSONRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet

from rest_framework.filters import OrderingFilter
from rest_framework_filters.backends import \
    ComplexFilterBackend, \
    RestFrameworkFilterBackend

from silk.profiling.profiler import silk_profile

from ...models import Model
from .filters import ModelFilter
from .queries import MODEL_REST_API_QUERY_SET
from .serializers import H1stModelSerializer


class H1stModelViewSet(ModelViewSet):
    queryset = MODEL_REST_API_QUERY_SET

    serializer_class = H1stModelSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    filter_class = ModelFilter

    filter_backends = \
        OrderingFilter, \
        ComplexFilterBackend, \
        RestFrameworkFilterBackend

    ordering_fields = \
        'uuid', \
        'created', \
        'modified'

    ordering = '-modified'

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name=f'{__module__}: {Model._meta.verbose_name_plural}')
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {Model._meta.verbose_name}')
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)