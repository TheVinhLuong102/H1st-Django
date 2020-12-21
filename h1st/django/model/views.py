from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import JsonResponse

from inspect import getsource
import json

from ..data.models import JSONDataSet
from ..data.util import load_data_set_pointers_as_json
from .models import H1stModel
from ..trust.models import Decision


def model_call_on_json_input_data(request, model_uuid, json_input_data):
    model = H1stModel.objects.get(uuid=model_uuid)

    json_input_data = json.loads(json_input_data)

    loaded_json_input_data = load_data_set_pointers_as_json(json_input_data)

    json_output_data = model(loaded_json_input_data)

    Decision.objects.create(
        input_data=json_input_data,
        model=model,
        model_code={str(model.uuid): getsource(type(model))},
        output_data=json_output_data)

    return JsonResponse(
            data=json_output_data,
            encoder=DjangoJSONEncoder,
            safe=True,
            json_dumps_params=None)
