from uuid import UUID

from .models import DataSet


def load_data_set_pointers_as_json(input_data: dict) -> dict:
    loaded_data = {}

    for k, v in input_data.items():
        if isinstance(v, dict):
            loaded_data[k] = load_data_set_pointers_as_json(v)

        elif isinstance(v, str):
            try:
                uuid = UUID(hex=v, version=4)
            except ValueError:
                uuid = None

            loaded_data[k] = \
                DataSet.objects.get(uuid=uuid).load() \
                if uuid \
                else v

        else:
            loaded_data[k] = v

    return loaded_data
