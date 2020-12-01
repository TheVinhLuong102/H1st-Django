from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import DataSchema, Dataset


@register(
    DataSchema,
    site=site)
class DataSchemaAdmin(ModelAdmin):
    pass


@register(
    Dataset,
    site=site)
class DatasetAdmin(ModelAdmin):
    pass
