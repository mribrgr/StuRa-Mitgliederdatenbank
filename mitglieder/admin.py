from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Mitglied, MitgliedMail, MitgliedAmt

admin.site.register(Mitglied, SimpleHistoryAdmin)
admin.site.register(MitgliedMail, SimpleHistoryAdmin)
admin.site.register(MitgliedAmt, SimpleHistoryAdmin)
