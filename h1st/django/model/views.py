from asgiref.sync import sync_to_async
from django.http.response import JsonResponse

import json

from .models import H1stDjangoModel


async def h1st_model_predict(request, h1st_model_uuid, input_data):
    h1st_model = await \
        sync_to_async(
            H1stDjangoModel.objects.get,
            thread_sensitive=False)(uuid=h1st_model_uuid)

    return JsonResponse(h1st_model.predict(json.loads(input_data)))
