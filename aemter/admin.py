from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from mitglieder.models import Mitglied, MitgliedMail, MitgliedAmt
from aemter.models import Organisationseinheit, Unterbereich, Funktion, Recht, FunktionRecht
from checklisten.models import Checkliste, Aufgabe, ChecklisteAufgabe, ChecklisteRecht

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


# Register your models here.
admin.site.register(Mitglied, SimpleHistoryAdmin)
admin.site.register(MitgliedMail, SimpleHistoryAdmin)
admin.site.register(MitgliedAmt, SimpleHistoryAdmin)

admin.site.register(Organisationseinheit, OrganisationseinheitAdmin)
admin.site.register(Unterbereich, UnterbereichAdmin)
#admin.site.register(Funktion, SimpleHistoryAdmin)
admin.site.register(Recht, SimpleHistoryAdmin)
admin.site.register(FunktionRecht, SimpleHistoryAdmin)

admin.site.register(Checkliste, SimpleHistoryAdmin)
admin.site.register(Aufgabe, SimpleHistoryAdmin)
admin.site.register(ChecklisteAufgabe, SimpleHistoryAdmin)
admin.site.register(ChecklisteRecht, SimpleHistoryAdmin)