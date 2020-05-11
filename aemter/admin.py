from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from mitglieder.models import Mitglied, MitgliedMail, MitgliedAmt
from aemter.models import Referat, Unterbereich, Amt, Recht, AmtRecht

# Register your models here.
admin.site.register(Mitglied, SimpleHistoryAdmin)
admin.site.register(MitgliedMail, SimpleHistoryAdmin)
admin.site.register(MitgliedAmt, SimpleHistoryAdmin)

admin.site.register(Referat, SimpleHistoryAdmin)
admin.site.register(Unterbereich, SimpleHistoryAdmin)
admin.site.register(Amt, SimpleHistoryAdmin)
admin.site.register(Recht, SimpleHistoryAdmin)
admin.site.register(AmtRecht, SimpleHistoryAdmin)
