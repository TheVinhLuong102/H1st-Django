from django.http.response import JsonResponse

import json

from ..data.models import JSONDataSet
from .models import H1stDjangoModel, Decision


def h1st_model_call(request, h1st_model_uuid, input_data):
    input_json = json.loads(input_data)

    json_data_set = JSONDataSet.objects.create(json=input_json)

    h1st_model = H1stDjangoModel.objects.get(uuid=h1st_model_uuid)

    decision_output_json = h1st_model(input_json)

    Decision.objects.create(
        data_set=json_data_set,
        h1st_model=h1st_model,
        output_json=decision_output_json)

    return JsonResponse(decision_output_json)
