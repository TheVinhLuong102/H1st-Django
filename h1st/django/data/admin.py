from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from silk.profiling.profiler import silk_profile

from .models import \
    DataSchema, \
    JSONDataSet, NamedJSONDataSet, \
    NamedCSVDataSet, NamedParquetDataSet, NamedTFRecordDataSet


@register(DataSchema, site=site)
class DataSchemaAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {DataSchema._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {DataSchema._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(JSONDataSet, site=site)
class JSONDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {JSONDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {JSONDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedJSONDataSet, site=site)
class NamedJSONDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {NamedJSONDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {NamedJSONDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedCSVDataSet, site=site)
class NamedCSVDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(
        name=f'{__module__}: {NamedCSVDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {NamedCSVDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedParquetDataSet, site=site)
class NamedParquetDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(
        name=f'{__module__}: {NamedParquetDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {NamedParquetDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedTFRecordDataSet, site=site)
class NamedTFRecordDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(
        name=f'{__module__}: {NamedTFRecordDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {NamedTFRecordDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)
