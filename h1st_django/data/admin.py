from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import Dataset


@register(
    Dataset,
    site=site)
class DatasetAdmin(ModelAdmin):
    pass
