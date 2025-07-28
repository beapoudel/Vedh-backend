from django.contrib import admin
from backend.models import images
class imageAdmin(admin.ModelAdmin):
    list_display=('name','email')
admin.site.register(images,imageAdmin)

# Register your models here.
