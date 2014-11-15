from django.contrib import admin
from gallery.models import Images, Gallery


class ImagesAdmin(admin.StackedInline):
    model = Images
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    exclude = ('created_date', 'modified_date')
    inlines = [ImagesAdmin]

admin.site.register(Gallery, GalleryAdmin)


