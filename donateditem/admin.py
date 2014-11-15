from django.contrib import admin
from donateditem.models import DonatedItem


class DonatedItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'status', 'created_date', 'modified_date', 'delivered_date', 'user_id', 'ashram_id')
    exclude = ('created_date', 'modified_date')

admin.site.register(DonatedItem, DonatedItemAdmin)