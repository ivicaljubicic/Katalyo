from django.contrib import admin

# Register your models here.
from .models import ResourceDef
from .models import ResourceDefLang
from .models import ResourceDefFields
from .models import ResourceDefFieldsLang
from .models import Organisations
from .models import Addresses

class OrganisationsAdmin(admin.ModelAdmin):
    list_display = ('pk','Name',)

admin.site.register(ResourceDef)
admin.site.register(ResourceDefLang)
admin.site.register(ResourceDefFields)
admin.site.register(ResourceDefFieldsLang)

admin.site.register(Organisations,OrganisationsAdmin)
admin.site.register(Addresses)