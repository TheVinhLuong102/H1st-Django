from rest_framework.authentication import \
    BasicAuthentication, \
    RemoteUserAuthentication, \
    SessionAuthentication, \
    TokenAuthentication
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import CoreJSONRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
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

    pagination_class = None

    parser_classes = JSONParser,

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name=f'{__module__}: {Model._meta.verbose_name_plural}')
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {Model._meta.verbose_name}')
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)


class ModelCallAPIView(APIView):
    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    parser_classes = \
        JSONParser, \
        MultiPartParser

    def post(self, request, *args, **kwargs):
        return Response(dict(

                request_parsing=dict(
                    data=str(request.data),
                    # DATA=str(request.DATA),

                    FILES=request.FILES,
                    POST=request.POST,

                    query_params=request.query_params,
                    # QUERY_PARAMS=str(request.QUERY_PARAMS),

                    # parsers=str(request.parsers)
                ),

                content_negotiation=dict(
                    accepted_renderer=str(request.accepted_renderer),
                    accepted_media_type=request.accepted_media_type
                ),

                authentication=dict(
                    user=str(request.user),
                    auth=request.auth,
                    # authenticators=str(request.authenticators)
                ),

                browser_enhancements=dict(
                    method=request.method,
                    content_type=request.content_type,
                    # stream=str(request.stream)
                )))
