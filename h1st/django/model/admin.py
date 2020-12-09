from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import H1stDjangoModel, Decision, H1stModelEvalMetricsSet


@register(
    H1stDjangoModel,
    site=site)
class H1stModelAdmin(ModelAdmin):
    pass


@register(
    Decision,
    site=site)
class DecisionAdmin(ModelAdmin):
    pass


@register(
    H1stModelEvalMetricsSet,
    site=site)
class H1stModelEvalMetricsSetAdmin(ModelAdmin):
    pass
