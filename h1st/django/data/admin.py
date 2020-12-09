from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import DataSchema, DataSet, JSONDataSet


@register(
    DataSchema,
    site=site)
class DataSchemaAdmin(ModelAdmin):
    pass


@register(
    DataSet,
    site=site)
class DataSetAdmin(ModelAdmin):
    pass


@register(
    JSONDataSet,
    site=site)
class JSONDataSetAdmin(ModelAdmin):
    pass
