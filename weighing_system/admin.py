from django.contrib import admin
from .models import Batch, WeighBridgeOffice
# Register your models here.


class WeighBridgeOfficeAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'weigh_house_name', )
    list_filter = ('company_name', )
    search_fields = ('company_name', 'weigh_house_name', )

admin.site.register(WeighBridgeOffice, WeighBridgeOfficeAdmin)
admin.site.register(Batch)
