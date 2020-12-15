from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import DataSchema, JSONDataSet, ParquetDataSet, TFRecordDataSet


@register(
    DataSchema,
    site=site)
class DataSchemaAdmin(ModelAdmin):
    pass


@register(
    JSONDataSet,
    site=site)
class JSONDataSetAdmin(ModelAdmin):
    pass


@register(
    ParquetDataSet,
    site=site)
class ParquetDataSetAdmin(ModelAdmin):
    pass


@register(
    TFRecordDataSet,
    site=site)
class TFRecordDataSetAdmin(ModelAdmin):
    pass
