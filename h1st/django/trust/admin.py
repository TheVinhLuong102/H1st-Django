from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import RecordedModelFittingRun, RecordedModelInferenceRun


@register(
    RecordedModelFittingRun,
    site=site)
class RecordedModelFittingRunAdmin(ModelAdmin):
    pass


@register(
    RecordedModelInferenceRun,
    site=site)
class RecordedModelInferenceRunAdmin(ModelAdmin):
    pass
