from django.core.files.uploadedfile import InMemoryUploadedFile

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

from inspect import getsource

from ....data.util import \
    load_data_set_pointers_as_json, \
    save_pandas_dfs_as_data_set_pointers
from ....trust.models import Decision
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
        try:
            model_uuid = request.data.pop('UUID')
        except:
            return Response("'UUID' Key Not Found in Request Body")

        try:
            assert isinstance(model_uuid, list) and (len(model_uuid) == 1)
        except:
            return Response(f"{model_uuid} Not Valid")

        model_uuid = model_uuid[0]

        try:
            model = Model.objects.get(uuid=model_uuid)
        except:
            return Response(f"Model with UUID #{model_uuid} Not Found")

        if request.content_type == 'application/json':
            json_input_data = request.data

            loaded_json_input_data = \
                load_data_set_pointers_as_json(json_input_data)

            json_output_data = model(loaded_json_input_data)

            saved_json_output_data = \
                save_pandas_dfs_as_data_set_pointers(json_output_data)

            Decision.objects.create(
                input_data=json_input_data,
                model=model,
                model_code={str(model.uuid): getsource(type(model))},
                output_data=saved_json_output_data)

            return Response(
                    data=saved_json_output_data,
                    status=None,
                    template_name=None,
                    headers=None,
                    exception=False,
                    content_type=None)

        elif request.content_type.startswith('multipart/form-data'):
            data = {}

            for k, v in request.data.items():
                if isinstance(v, InMemoryUploadedFile):
                    data[k] = dict(name=v.name, content_type=v.content_type)

                elif isinstance(v, (list, tuple)) and \
                        all(isinstance(i, InMemoryUploadedFile)
                            for i in v):
                    data[k] = [dict(name=i.name, content_type=i.content_type)
                               for i in v]

                else:
                    data[k] = v

            return Response(dict(

                    request_parsing=dict(
                        data=data,
                        # DATA=str(request.DATA),

                        # FILES=request.FILES,
                        # POST=request.POST,

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

        else:
            return Response('Content Type must be '
                            "either 'application/json' "
                            "or 'multipart/form-data'")
