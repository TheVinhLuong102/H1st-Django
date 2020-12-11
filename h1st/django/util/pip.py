from pip._internal.operations.freeze import freeze


def get_python_dependencies():
    return list(freeze())
