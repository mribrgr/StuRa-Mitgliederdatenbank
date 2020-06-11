from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from mitglieder.models import Mitglied, MitgliedMail, MitgliedAmt
from aemter.models import Organisationseinheit, Unterbereich, Funktion, Recht, AmtRecht

# Register your models here.
admin.site.register(Mitglied, SimpleHistoryAdmin)
admin.site.register(MitgliedMail, SimpleHistoryAdmin)
admin.site.register(MitgliedAmt, SimpleHistoryAdmin)

admin.site.register(Organisationseinheit, SimpleHistoryAdmin)
admin.site.register(Unterbereich, SimpleHistoryAdmin)
admin.site.register(Funktion, SimpleHistoryAdmin)
admin.site.register(Recht, SimpleHistoryAdmin)
admin.site.register(AmtRecht, SimpleHistoryAdmin)
