from django.contrib import admin

from .models import Region, DataType, DataSource, Units, TminMonthWise, TmaxMonthWise, \
    TmeanMonthWise, RainfallMonthWise, SunshineMonthWise
from .tasks import download_data


class DatatyeAdmin(admin.ModelAdmin):
    list_display = ['name']


class UnitsAdmin(admin.ModelAdmin):
    list_display = ['name']


class DataSourceAdmin(admin.ModelAdmin):
    list_display = ['url']


class TminMonthWiseAdmin(admin.ModelAdmin):
    list_display = ['region', 'year', 'month', "value", "unit"]


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    actions = ['download_data']

    def download_data(self, request, queryset):

        data_source = DataSource.objects.filter(region__in=queryset)
        urls = [(each.url, each.data_type.name, each.region.id, each.unit.id) for each in data_source]
        # urls = []
        # for each in data_source:
        #     print(each)
        #     urls.append((each.url, each.data_type.name, each.region.id. each.unit.id))
        download_data.delay(urls, request.user.username)


admin.site.register(DataSource, DataSourceAdmin)
admin.site.register(DataType, DatatyeAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Units, UnitsAdmin)
admin.site.register(TminMonthWise, TminMonthWiseAdmin)


