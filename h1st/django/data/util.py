import json
from numpy import ndarray
from pandas import DataFrame
from uuid import UUID

from .models import DataSet, NumPyArray, PandasDataFrame


def load_data_set_pointers_as_json(data):
    if isinstance(data, dict):
        return {k: load_data_set_pointers_as_json(v)
                for k, v in data.items()}

    elif isinstance(data, (list, tuple)):
        return [load_data_set_pointers_as_json(i)
                for i in data]

    elif isinstance(data, str):
        try:
            uuid = UUID(hex=data, version=4)
        except ValueError:
            uuid = None

        return DataSet.objects.get(uuid=uuid).load() \
            if uuid \
          else data

    else:
        return data


def save_numpy_arrays_and_pandas_dfs_as_data_set_pointers(data):
    if isinstance(data, dict):
        return {k: save_numpy_arrays_and_pandas_dfs_as_data_set_pointers(v)
                for k, v in data.items()}

    elif isinstance(data, (list, tuple)):
        return [save_numpy_arrays_and_pandas_dfs_as_data_set_pointers(i)
                for i in data]

    elif isinstance(data, ndarray):
        return NumPyArray.objects.create(
                dtype=str(data.dtype),
                json=data.tolist()).uuid

    elif isinstance(data, DataFrame):
        return PandasDataFrame.objects.create(
                json=json.loads(data.to_json(path_or_buf=None,
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
        return data
