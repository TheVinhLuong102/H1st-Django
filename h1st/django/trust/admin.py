from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import \
    ImmutableJSONDataSet, ImmutableParquetDataSet, \
    Decision, \
    ModelEvalMetricsSet


@register(
    ImmutableJSONDataSet,
    site=site)
class ImmutableJSONDataSetAdmin(ModelAdmin):
    pass


@register(
    ImmutableParquetDataSet,
    site=site)
class ImmutableParquetDataSetAdmin(ModelAdmin):
    pass


@register(
    Decision,
    site=site)
class DecisionAdmin(ModelAdmin):
    pass


@register(
    ModelEvalMetricsSet,
    site=site)
class ModelEvalMetricsSetAdmin(ModelAdmin):
    pass
