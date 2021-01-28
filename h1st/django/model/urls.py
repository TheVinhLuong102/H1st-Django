from django.urls.conf import include, path

from rest_framework.routers import DefaultRouter

from .api.rest.views import H1stModelViewSet
from .views import model_call_on_json_input_data


CORE_REST_API_ROUTER = DefaultRouter(trailing_slash=False)

CORE_REST_API_ROUTER.register(
    prefix='models',
    viewset=H1stModelViewSet,
    basename=None)


urlpatterns = [
    path('api/rest/',
         include(CORE_REST_API_ROUTER.urls)),

    path(route='<str:model_uuid>/<str:json_input_data>/',
         view=model_call_on_json_input_data)
]
