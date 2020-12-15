from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from silk.profiling.profiler import silk_profile

from .models import DataSchema, JSONDataSet, ParquetDataSet, TFRecordDataSet


@register(DataSchema, site=site)
class DataSchemaAdmin(ModelAdmin):
    list_display = \
        'name', \
        'specs', \
        'modified'

    list_display_links = \
        'name', \
        'specs'

    search_fields = \
        'name', \
        'specs'

    show_full_result_count = False

    readonly_fields = \
        'created', \
        'modified'

    def get_queryset(self, request):
        query_set = super().get_queryset(request=request)

        return query_set \
            if request.resolver_match.url_name.endswith('_change') \
          else query_set.only(*self.list_display)

    @silk_profile(name=f'{__module__}: {DataSchema._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {DataSchema._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(JSONDataSet, site=site)
class JSONDataSetAdmin(ModelAdmin):
    list_display = \
        'name', \
        'schema__name', \
        'modified'

    list_display_links = 'name',

    search_fields = 'name',

    show_full_result_count = False

    readonly_fields = \
        'created', \
        'modified'

    def get_queryset(self, request):
        query_set = super().get_queryset(request=request)

        return query_set \
            if request.resolver_match.url_name.endswith('_change') \
          else query_set.only(*self.list_display)

    @silk_profile(name=f'{__module__}: {JSONDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {JSONDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(ParquetDataSet, site=site)
class ParquetDataSetAdmin(ModelAdmin):
    list_display = \
        'name', \
        'schema__name', \
        'modified'

    list_display_links = 'name',

    search_fields = 'name',

    show_full_result_count = False

    readonly_fields = \
        'created', \
        'modified'

    def get_queryset(self, request):
        query_set = super().get_queryset(request=request)

        return query_set \
            if request.resolver_match.url_name.endswith('_change') \
          else query_set.only(*self.list_display)

    @silk_profile(name=f'{__module__}: {ParquetDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {ParquetDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(TFRecordDataSet, site=site)
class TFRecordDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {TFRecordDataSet._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {TFRecordDataSet._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)
