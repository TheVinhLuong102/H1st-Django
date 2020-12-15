from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from silk.profiling.profiler import silk_profile

from .models import \
    ImmutableJSONDataSet, ImmutableParquetDataSet, ImmutableTFRecordDataSet, \
    Decision, \
    ModelEvalMetricsSet


@register(
    ImmutableJSONDataSet,
    site=site)
class ImmutableJSONDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(
        name=f'{__module__}: {ImmutableJSONDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {ImmutableJSONDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(
    ImmutableParquetDataSet,
    site=site)
class ImmutableParquetDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(
        name=f'{__module__}: {ImmutableParquetDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: '
             f'{ImmutableParquetDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(
    ImmutableTFRecordDataSet,
    site=site)
class ImmutableTFRecordDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(
        name=f'{__module__}: {ImmutableTFRecordDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: '
             f'{ImmutableTFRecordDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(
    Decision,
    site=site)
class DecisionAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {Decision._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {Decision._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(
    ModelEvalMetricsSet,
    site=site)
class ModelEvalMetricsSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(
        name=f'{__module__}: {ModelEvalMetricsSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {ModelEvalMetricsSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)
