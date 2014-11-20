from django.contrib import admin
from ashrams.models import Ashrams


class AshramAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'address', 'phone', 'strength', ('below_one', 'one_to_five', 'six_to_ten',
                                                                    'eleven_to_fourteen', 'fifteen_to_eighteen',
                                                                    'nineteen_to_forty'), ('forty_to_sixty',
                                                                                           'above_sixty'),
                           'ashram_rating', 'username', 'ashram_pic')}),
    )
    list_display = ('id', 'name', 'address', 'phone', 'username', 'strength')
admin.site.register(Ashrams, AshramAdmin)
