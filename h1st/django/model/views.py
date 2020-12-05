from django.http.response import JsonResponse

import json

from .models import H1stDjangoModel


def h1st_model_predict(request, h1st_model_uuid, input_data):
    h1st_model = H1stDjangoModel.objects.get(uuid=h1st_model_uuid)
    return JsonResponse(h1st_model.predict(json.loads(input_data)))
