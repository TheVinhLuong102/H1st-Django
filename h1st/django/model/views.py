from django.http.response import JsonResponse

import json

from ..data.models import JSONDataSet
from .models import H1stDjangoModel, Decision


def h1st_model_predict(request, h1st_model_uuid, input_data):
    json_data_set = JSONDataSet.objects.create(json=input_data)

    h1st_model = H1stDjangoModel.objects.get(uuid=h1st_model_uuid)

    decision_output = h1st_model.predict(json.loads(input_data))

    decision = \
        Decision.objects.create(
            data_set=json_data_set,
            h1st_model=h1st_model,
            output_json=decision_output)

    return JsonResponse(decision.output_json)
