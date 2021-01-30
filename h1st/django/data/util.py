import json
from numpy import ndarray
from pandas import DataFrame
from uuid import UUID

from .models import DataSet, NumPyArray, PandasDataFrame


def load_data_set_pointers_as_json(data: dict) -> dict:
    loaded_data = {}

    for k, v in data.items():
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


def save_numpy_arrays_and_pandas_dfs_as_data_set_pointers(data: dict) -> dict:
    data_with_pointers = {}

    for k, v in data.items():
        if isinstance(v, dict):
            data_with_pointers[k] = load_data_set_pointers_as_json(v)

        elif isinstance(v, (list, tuple)):
            data_with_pointers[k] = \
                [load_data_set_pointers_as_json(i)
                 for i in v]

        elif isinstance(v, ndarray):
            data_with_pointers[k] = \
                NumPyArray.objects.create(
                    dtype=v.dtype,
                    json=v.tolist()).uuid

        elif isinstance(v, DataFrame):
            data_with_pointers[k] = \
                PandasDataFrame.objects.create(
                    json=json.loads(v.to_json(path_or_buf=None,
                                              orient='split',
                                              date_format='iso',
                                              double_precision=10,
                                              force_ascii=False,
                                              date_unit='ms',
                                              default_handler=None,
                                              lines=False,
                                              compression=None,
                                              index=True,
                                              indent=None,
                                              storage_options=None))).uuid

        else:
            data_with_pointers[k] = v

    return data_with_pointers
