from django.contrib import admin
from requireditem.models import RequiredItem


class RequiredItemAdmin(admin.ModelAdmin):
    exclude = ('created_date', 'modified_date')
    list_display = ('name', 'created_date', 'modified_date', 'ashram_id')

admin.site.register(RequiredItem, RequiredItemAdmin)