from django.urls.conf import path

from .views import model_call_on_json_input_data


urlpatterns = [
    path(route='<str:model_uuid>/<str:json_input_data>/',
         view=model_call_on_json_input_data)
]
