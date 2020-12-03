from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import H1stModel, H1stModelEvalMetricsSet


@register(
    H1stModel,
    site=site)
class H1stModelAdmin(ModelAdmin):
    pass


@register(
    H1stModelEvalMetricsSet,
    site=site)
class H1stModelEvalMetricsSetAdmin(ModelAdmin):
    pass