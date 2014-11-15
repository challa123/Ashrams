from django.contrib import admin
from anonymoususer.models import AnonymousUser


class AnonymousUserAdmin(admin.ModelAdmin):
    exclude = ('created_date', 'modified_date')
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email')

admin.site.register(AnonymousUser, AnonymousUserAdmin)
