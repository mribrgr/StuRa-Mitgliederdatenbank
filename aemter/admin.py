from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Organisationseinheit, Unterbereich, Funktion, Recht, FunktionRecht

# Custom model admins
class InLineUnterbereich(admin.TabularInline):
    model = Unterbereich
    extra = 0

class InLineFunktionOrganisationseinheit(admin.TabularInline):
    model = Funktion
    exclude = ('unterbereich',)
    extra = 0

class InLineFunktionUnterbereich(admin.TabularInline):
    model = Funktion
    exclude = ('organisationseinheit',)
    extra = 0

class OrganisationseinheitAdmin(SimpleHistoryAdmin):
    inlines = [InLineFunktionOrganisationseinheit, InLineUnterbereich]

class UnterbereichAdmin(SimpleHistoryAdmin):
    inlines = [InLineFunktionUnterbereich]

admin.site.register(Organisationseinheit, OrganisationseinheitAdmin)
admin.site.register(Unterbereich, UnterbereichAdmin)
admin.site.register(Recht, SimpleHistoryAdmin)
admin.site.register(FunktionRecht, SimpleHistoryAdmin)