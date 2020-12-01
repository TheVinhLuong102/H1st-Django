from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import Decision


@register(
    Decision,
    site=site)
class DecisionAdmin(ModelAdmin):
    pass
