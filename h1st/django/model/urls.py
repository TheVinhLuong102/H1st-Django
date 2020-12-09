from django.urls.conf import path

from .views import h1st_model_call


urlpatterns = [
    path('<str:h1st_model_uuid>/<str:input_data>/', h1st_model_call)
]
